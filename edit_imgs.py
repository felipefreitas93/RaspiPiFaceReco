"""
Felipe Freitas de Carvalho
TCC - Reconhecimento facial utilizando o raspberry pi

Scrip para editar as imagens contidas na pasta .training/capture para que estas
estejam adequadas para serem treinadas
"""
import variables
import cv2
import os

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

def editimgs(pathcap,pathpos):
    count = 1
    for root, dirs, files in os.walk(pathcap,pathpos):
        for filename in files:
            fullpath = root + '/' + filename
            image = cv2.imread(fullpath)
            image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
            coords = recon_face(image)
            if coords !=None:
                x,y,w,h = coords
                image = cut_resize(image,x,y,w,h)
                writepath = pathpos + '/' + str(count) + '.pgm'
                print(writepath)
                count += 1
                cv2.imwrite(writepath,image)
            else:
                print('imagem em {} nao teve a face reconhecida'.format(fullpath))
            


if __name__ == '__main__':
    #Cria o diretorio para as imagens positivas caso este
    #nao exista ainda
    if not os.path.exists(variables.path_positive):
        os.makedirs(variables.path_positive)

    editimgs(variables.path_capture, variables.path_positive)
    
                
            
        
    



