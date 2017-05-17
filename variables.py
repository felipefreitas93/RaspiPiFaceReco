"""
Felipe Freitas de Carvalho
TCC - Reconhecimento facial utilizando o raspberry pi

Arquivo que contem variaveis pertinentes ao projeto para serem usadas em outros
scrips e funcoes
"""

#caminho para as capturas com a camera (manualmente ou pelo script)
path_capture = './training/capture'
#exemplos positivos e negativos
path_positive = './training/positive'
path_negative = './training/negative'
#labels para exemplos positivos e negativos
positive_label = 1
negative_label = 0
#extrator de face pre-treinado
cascade = 'haarcascade_frontalface_alt.xml'
#parametros padrao para o cascade
haar_scale_factor  = 1.1
haar_min_neighbors = 5
haar_min_size      = (30, 30)
#tamanho padrao das imagens das faces (que deve ser consistente com a database
#de faces que servirao de exemplos negativos) - AT&T database
#http://www.cl.cam.ac.uk/research/dtg/attarchive/facedatabase.html
face_width  = 92
face_height = 112
#modelo trainado salvo
trained_model = 'trained_model.xml'
#GPIO pinos usados para o sensor
trig = 4
echo = 17
#distancia limite inferior e superior
distance = [20,45]
#pino do led verde
ledpingreen = 24
ledpinred = 18
#n de vezes que o led pisca
ntimes = 3
#tempo entre cada piscada
tled = 0.3
