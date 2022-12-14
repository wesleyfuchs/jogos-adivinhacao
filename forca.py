# forca.py

import random


def jogar():
    mensagem_introducao()
    palavra_secreta = carregar_palavra_secreta()
    letras_acertadas = inicializar_letras_acertadas(palavra_secreta)
    letras_utilizadas = []
    erros = 0
    
    print(letras_acertadas)
    
    # while erros < 7 ou _ not in letras acertadas
    while True:
        chute = pedir_chute()

        if (chute not in letras_utilizadas):
            if (chute in palavra_secreta):
                index = 0
                for letra in palavra_secreta:
                    if (chute == letra):
                        letras_acertadas[index] = letra
                    index += 1
            else:
                erros += 1
                desenha_forca(erros)
        else:
            print("Essa letra ja foi utlizada!!!")
            print(list(set(letras_utilizadas)))

        letras_utilizadas.append(chute)
        
        #Checa se ganhou ou perdeu
        if (erros == 7):
            break
        if ("_" not in letras_acertadas):
            break

        print(letras_acertadas)
    #Fim programa principal
    
    # Mensagem de vitoria/derrota
    if ("_" not in letras_acertadas):
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(palavra_secreta)
        
    print("Fim do jogo")


def mensagem_introducao():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")


def carregar_palavra_secreta():
    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()

    return palavra_secreta


def inicializar_letras_acertadas(palavra):
    return ["_" for letra in palavra]


def pedir_chute():
    chute = input("Qual letra? ")
    chute = chute.strip().upper()  # tratar entrada (tirar espaços da entrada, deixar maiusculo)
    return chute


def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


def imprime_mensagem_vencedor():
    print("Você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def imprime_mensagem_perdedor(palavra):
    print("A palavra era {}".format(palavra))
    print("Você perdeu!")


if (__name__ == "__main__"):  #sempre colocar no fim do arquivo
    jogar()

