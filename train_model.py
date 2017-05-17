"""
Felipe Freitas de Carvalho
TCC - Reconhecimento facial utilizando o raspberry pi

Scrip cujo o objetivo e treinar um modelo e salva-lo como um arquivo
xml utilizando as imagens positivas e negativas contidas na pasta training
"""

import cv2
import os
import variables
import numpy



def train_model():

    examples = []
    labels = []
    

    count_pos = 0
    for root, dirs, files in os.walk(variables.path_positive):
        for filename in files:
            fullpath = root + '/' + filename
            image = cv2.imread(fullpath, cv2.IMREAD_GRAYSCALE)
            examples.append(numpy.asarray(image))
            labels.append(1)
            count_pos += 1
    print("Foram obtidas {} faces positivas".format(count_pos))
    
    count_neg = 0
    for root, dirs, files in os.walk(variables.path_negative):
        for subdirs in dirs:
            allpaths = root + '/' + subdirs
            for filename in os.listdir(allpaths):
            #each image in path (eiip)
                eiip = allpaths + '/' + filename
                image = cv2.imread(eiip,cv2.IMREAD_GRAYSCALE)
                examples.append(numpy.asarray(image))
                labels.append(0)
                count_neg += 1
    print("Foram obtidas {} faces negativas".format(count_neg))

    print("Treinando modelo...")
    #model = cv2.createEigenFaceRecognizer()
    model = cv2.createLBPHFaceRecognizer()
    model.train(examples,numpy.asarray(labels))
    model.save(variables.trained_model)

    print("Modelo salvo como {}".format(variables.trained_model))
            
if __name__ == '__main__':
    train_model()
