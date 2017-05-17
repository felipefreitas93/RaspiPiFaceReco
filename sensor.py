"""
Felipe Freitas de Carvalho
TCC - Reconhecimento facial utilizando o raspberry pi

Scrip que contem a funcao que ativa o sensor ultrassonico e calcula
a distancia de um objeto deste. Caso este objeto esteja entre valores
desejados a funcao retorna True
"""

import variables
import RPi.GPIO as GPIO
import time


def sensor(trig,echo,distance,sleep=2):
  
  #modo de chamar os pinos
  GPIO.setmode(GPIO.BCM)
  #setar os pinos como entrada ou saida
  GPIO.setwarnings(False)
  GPIO.setup(trig,GPIO.OUT)
  GPIO.setup(echo,GPIO.IN)

  while True:
    #desliga o trigger
    GPIO.output(trig, False)
    time.sleep(sleep)
    #pulso de 10us no trigger para medir a distancia
    GPIO.output(trig, True)
    time.sleep(0.00001)
    GPIO.output(trig, False)

    #duracao do sinal ir e voltar
    while GPIO.input(echo)==0:
      inicio = time.time()
    while GPIO.input(echo)==1:
      final = time.time()
    duracao = final - inicio

    distancia = duracao * 17150
    print(distancia)

    if(distancia>distance[0] and distancia<distance[1]):
      print("Distancia de {} cm".format(distancia))
      return True
    


if __name__=="__main__":
  a = sensor(variables.trig,variables.echo,variables.distance)
            
