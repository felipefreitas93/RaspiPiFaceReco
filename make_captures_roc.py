"""
Felipe Freitas de Carvalho
TCC - Reconhecimento facial utilizando o raspberry pi

Scrip para capturar imagens para a pasta roc que serao utilizadas
para construir a curva ROC para analise do algoritmo
"""

from picamera import PiCamera
import cv2
import os
import io
from time import sleep
import numpy as np

path = "/home/pi/Desktop/TCC/roc/roccapture"


if __name__ == "__main__":
    if not os.path.exists(path):
        os.makedirs(path)

    camera = PiCamera()

    count_cap = 0
    while True:
        decisao = input("Digite 1 para capturar uma imagem ou 2 para sair: ")
        if decisao == 1:
            sleep(1)
            camera.capture(path + '/capture' + str(count_cap) + '.jpg')
            count_cap += 1
            print("{} imagens ja capturadas".format(count_cap))
        elif decisao == 2:
            print("Verifique as imagens capturadas em {}".format(path))
            break
        else:
            print("Opcao invalida, digite novamente")
            continue

