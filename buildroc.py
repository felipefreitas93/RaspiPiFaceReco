"""
Felipe Freitas de Carvalho
TCC - Reconhecimento facial utilizando o raspberry pi

Scrip para realizar todos os passos necessarios para construcao da curva ROC,
que envolvem o tratamento das imagens a serem utilizados e a passagem das
mesmas pelo detector.
"""

from sklearn.metrics import roc_curve, auc
import matplotlib.pyplot as plt
import variables
import cv2
import os
import numpy as np


def recon_face(image):
    '''Retorna as coordenadas, largura e altura de uma cara
detectada, caso mais de uma cara seja detectada retorna None
'''
    haar = cv2.CascadeClassifier(variables.cascade)

    coords = haar.detectMultiScale(image,
                                   scaleFactor=variables.haar_scale_factor,
                                   minNeighbors=variables.haar_min_neighbors,
                                   minSize=variables.haar_min_size,
                                   flags=cv2.CASCADE_SCALE_IMAGE)
    if len(coords) != 1:
        return None
    return coords[0]

def cut_resize(image, x, y, w, h):
    '''Recorta a cara da imagem, definida pelas coords (x,y,w,h)
sendo (x,y) o canto esquero superior. Alem disso, mantem o mesmo
aspect ratio das imagens negativas usadas para treinamento. Depois,
altera o tamanho da imagem para o mesmo das imagens negativas
'''
    height = int((variables.face_height / float(variables.face_width)) * w)
    meioy = int(y + h/2)
    y1 = int(max(0, meioy - height/2))
    y2 = int(min(image.shape[0]-1, meioy + height/2))
    image = image[y1:y2, x:x+w]
    image = cv2.resize(image,(variables.face_width,variables.face_height),
                       interpolation=cv2.INTER_LANCZOS4)
    return image


if __name__ == '__main__':

    model = cv2.createLBPHFaceRecognizer()
    model.load(variables.trained_model)
    
    print("Modelo carregado")
    print("Construindo a curva ROC")

    #labels de cada imagem
    labels = []
    #classe de saida
    output = []
    #saida do lpb (baseado em distancia)
    confidence = []

    
    nofacecounter = 0
    for root, dirs, files in os.walk("/home/pi/Desktop/TCC/roc/roctrain"):
        for subdirs in dirs:
            allpaths = root + '/' + subdirs
            for filename in os.listdir(allpaths):
                #each image in path (eiip)
                eiip = allpaths + '/' + filename
                if "myface" in eiip:
                    labels.append(1)
                else:
                    labels.append(0)
                image = cv2.imread(eiip)
                image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
                coords = recon_face(image)
                if coords !=None:
                    #reconheceu a face
                    x,y,w,h = coords
                    image = cut_resize(image,x,y,w,h)
                    classe, threshold = model.predict(image)
                    output.append(classe)
                    confidence.append(threshold)
                    
                else:
                    #nao reconheceu a face
                    output.append(0)
                    confidence.append(0)
                    print(eiip + " nao reconhecida")
                    nofacecounter += 1

    print("{} faces nao foram detectadas".format(nofacecounter))

    #valores de 0 a 1 para saida do algoritmo, normalizados pela distancia
    predictions = []
    #valor maximo de distancia para normalizar
    maxvalue = max(confidence)
    
    
    for classeout, distancia in zip(output, confidence):
        if classeout == 1:
            result = (2*maxvalue - distancia)/(2.0*maxvalue)
            predictions.append(result)
        elif classeout == 0:
            result = distancia/(2.0*maxvalue)
            predictions.append(result)
            
        

    false_positive_rate, true_positive_rate, thresholds = roc_curve(labels, predictions)
    roc_auc = auc(false_positive_rate, true_positive_rate)

    plt.title('Receiver Operating Characteristic')
    plt.plot(false_positive_rate, true_positive_rate, 'b',
    label='AUC = %0.2f'% roc_auc)
    plt.legend(loc='lower right')
    plt.plot([0,1],[0,1],'r--')
    plt.ylabel('True Positive Rate')
    plt.xlabel('False Positive Rate')
    plt.show()
    plt.savefig("ROC.jpg")
