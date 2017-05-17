"""
Felipe Freitas de Carvalho
TCC - Reconhecimento facial utilizando o raspberry pi

Scrip para capturar imagens para a pasta capture que serao utilizadas
posteriormente como o grupo de imagens positivas
"""

if __name__ == "__main__":
    from picamera import PiCamera
    camera = PiCamera()
    from time import sleep
    import variables
    import os

    if not os.path.exists(variables.path_capture):
        os.makedirs(variables.path_capture)


    #dependendo da orientacao da camera e necessario vira-la verticalmente
    camera.vflip = True

    count_cap = 0
    while True:
        decisao = input("Digite 1 para capturar uma imagem ou 2 para sair: ")
        if decisao == 1:
            sleep(1)
            camera.capture(variables.path_capture + '/capture' + str(count_cap) + '.jpg')
            count_cap += 1
            print("{} imagens ja capturadas".format(count_cap))
        elif decisao == 2:
            print("Verifique as imagens capturadas em {}".format(variables.path_capture))
            break
        else:
            print("Opcao invalida, digite novamente")
            continue

