import random

def jogar():                    #Função responsável por executar o jogo abrindo todas as outras funções
    abertura()
    palavra_secreta = carrega_palavra_secreta()
    lista_letras = letras_acertadas(palavra_secreta)
    regras(palavra_secreta, lista_letras)
    print("Fim do jogo")

def abertura():             #Abre uma mensagem de abertura
    print("*********************************")
    print("Bem vindo ao jogo de Forca!")
    print("*********************************\n")
    print("Uma dica: As palavras referem-se a frutas!")

def carrega_palavra_secreta():          #Lê um arquivo txt que contém as palavras do jogo
    arquivo = open("Frutas.txt", "r")
    palavras = []
    for linha in arquivo:
        palavras.append(linha.strip().upper())
    arquivo.close()
    palavra_secreta = palavras[random.randrange(0, len(palavras))]
    return palavra_secreta

def letras_acertadas(palavra):          #Transforma a palavra numa lista do formato ['_', '_', '_', '_']
    return ["_" for letra in palavra]

def regras(palavra_secreta, lista_letras):      #Define as regras do jogo: 7 chutes
    erros = 0
    enforcou = False
    acertou = False
    while (not enforcou) and (not acertou):
        chute = input("\nEntre com uma letra para a forca: ").strip().upper()
        index = 1
        lista = []
        if (chute in palavra_secreta) and (chute not in lista_letras):
            palavra_certa(palavra_secreta,chute, lista, lista_letras, index)
        else:
            erros = erros + 1
            desenha_forca(erros)
        enforcou = erros == 7
        acertou = "_" not in lista_letras
        if not acertou:
            print("Ainda faltam acertar {} letras".format(lista_letras.count("_")))
        if (not enforcou):
            print("Você ainda tem {} chance(s) até ser enforcado.".format(7 - erros))

        print(lista_letras)
    if (acertou):
        mensagem_vencedor()
    else:
        mensagem_perdedor(palavra_secreta)

def palavra_certa(palavra_secreta,chute, lista, lista_letras, index):       #introduz a letra acertada na lista ['_', '_', '_', '_']
    for letra in palavra_secreta:
        if (chute == letra):
            lista.append(index)
            lista_letras[index - 1] = chute
    print("\nVocê acertou a letra {} que está na(s) posição(ões) {}".format(chute, lista))

def mensagem_vencedor():    #imprime uma mensagem para o vencedor
    print("\n\nParabéns, você ganhou!")
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

def mensagem_perdedor(palavra_secreta):     #imprime uma mensagem caso não acerte todas as letras
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def desenha_forca(erros):       #imprime a forca a cada erro do usuário
    print("Você errou!\n\n")
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

if (__name__ == "__main__"):
    jogar()
