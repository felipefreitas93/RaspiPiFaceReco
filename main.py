#!/usr/bin/python2

import picamera
import cv2
import variables
import numpy as np
import io
import time
import edit_imgs
import sensor
import ledblink


def cameracap():
    stream = io.BytesIO()
    with picamera.PiCamera() as camera:
        #dependendo da orientacao da camera e necessario vira-la verticalmente
        #camera.vflip = True
        camera.capture(stream, format='jpeg')
    data = np.fromstring(stream.getvalue(), dtype=np.uint8)
    image = cv2.imdecode(data, 1)
    return image


if __name__ == "__main__":
    print("Scrip para reconhecimento facial de um usuario cadastrado")
    print("Para sair do scrip digite ctrl-c")
    #model = cv2.createEigenFaceRecognizer()
    model = cv2.createLBPHFaceRecognizer()
    model.load(variables.trained_model)
    print("Modelo carregado")
    while True:
        a = sensor.sensor(variables.trig,variables.echo,variables.distance)
        if a == True:            
            image = cameracap()
            cv2.imwrite("last_capture.jpg",image)
            print("Imagem capturada")
        #cv2.imshow("image",image)
        #cv2.waitKey(0) & 0xFF
        #cv2.destroyAllWindows()
            image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
            face = edit_imgs.recon_face(image)
            if face is None:
                print("Nao foi detectada nenhuma face ou foi detectado mais de um usuario")
                continue
            x, y, w, h = face
            image = edit_imgs.cut_resize(image, x, y, w, h)
            print("Face detectada, reconhecendo...")
            label, confidence = model.predict(image)
            print("Imagem reconhecida como pertencente a class {} com confianca {}".format(label,confidence))
            if label == 1:
                ledblink.ledblink(variables.ledpingreen,variables.ntimes,variables.tled)
            elif label == 0:
                ledblink.ledblink(variables.ledpinred,variables.ntimes,variables.tled)

            
        
        
    
