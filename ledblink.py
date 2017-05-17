import variables

def ledblink(pin,n,t):
    '''Funcao que faz um led piscar, pin e o pino GPIO onde o led esta
    conectado, n e o numero de vezes que o led pisca e t e o tempo entre
    cada piscada do led
    '''
    import RPi.GPIO as GPIO
    import time
    GPIO.setmode(GPIO.BCM)

    GPIO.setwarnings(False)

    GPIO.setup(pin,GPIO.OUT)
    GPIO.output(pin,False)
    for i in range(1,n+1):
        GPIO.output(pin,True)
        time.sleep(t/2)
        GPIO.output(pin,False)
        time.sleep(t/2)

if __name__ == '__main__':
    ledblink(variables.ledpingreen,variables.ntimes,variables.tled)
