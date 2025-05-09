def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    palavra_enforca = "cupuaçu"

    enforcou = False
    acertou = False

    while (not enforcou and not acertou):
        chute = input ("qual é a letra?")
        chute = chute.strip()

        posicao = 0
        for letra in palavra_enforca:
            if(chute.upper() == letra.upper()):
                print(f'encontrei a letra {letra} na posiçao{posicao}')
                posicao = posicao + 1

        print ("jogando...")  

    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()
