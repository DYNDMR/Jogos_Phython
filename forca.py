
import random



def jogar():
 
    boas_vindas()
    palavra_secreta = carrega_palavras()
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    print(letras_acertadas)

    enforcou = False
    acertou = False
    tentativas = 0

    
    while(not enforcou and not acertou):
        
        chute = pede_chute()

        if(chute in palavra_secreta):
          i = 0
          for letra in palavra_secreta:
                if(chute == letra):
                    letras_acertadas [i] = letra
                i += 1
        else:
            tentativas += 1
            desenha_forca(tentativas)

        enforcou = tentativas == 7   
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

        
    if(acertou):
        mensagem_ganhou()
    else:
        mensagem_enforcou(palavra_secreta)


    



#funçoes

def boas_vindas():
    print("**********************************")
    print("...Bem vindos ao jogo de Forca!...")
    print("**********************************")

def carrega_palavras():
    arquivo = open("palavras_aleatorias.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()
    
    index = random.randrange(0,len(palavras))
    palavra_secreta = palavras[index].upper()
    return palavra_secreta

def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]   

def pede_chute():
    chute = input("Digite uma letra: ")
    chute = chute.strip().upper()
    return chute

def mensagem_enforcou(palavra_secreta):
    print("")
    print("")
    print("............FORCA..............")
    print("..........Você perdeu!.........")
    print("A palavra era: {}".format(palavra_secreta))
    print("████▀░░░░░░░░░░░░░░░░░▀████")
    print("███│░░░░░░░░░░░░░░░░░░░│███")
    print("██▌│░░░░░░░░░░░░░░░░░░░│▐██")
    print("██░└┐░░░░░░░░░░░░░░░░░┌┘░██")
    print("██░░└┐░░░░░░░░░░░░░░░┌┘░░██")
    print("██░░┌┘▄▄▄▄▄░░░░░▄▄▄▄▄└┐░░██")
    print("██▌░│██████▌░░░▐██████│░▐██")
    print("███░│▐███▀▀░░▄░░▀▀███▌│░███")
    print("██▀─┘░░░░░░░▐█▌░░░░░░░└─▀██")
    print("██▄░░░▄▄▄▓░░▀█▀░░▓▄▄▄░░░▄██")
    print("████▄─┘██▌░░░░░░░▐██└─▄████")
    print("█████░░▐█─┬┬┬┬┬┬┬─█▌░░█████")
    print("████▌░░░▀┬┼┼┼┼┼┼┼┬▀░░░▐████")
    print("█████▄░░░└┴┴┴┴┴┴┴┘░░░▄█████")
    print("███████▄░░░░░░░░░░░▄███████")


def mensagem_ganhou():
    print("................PARABÉNS!................")
    print("...............Você ganhou!..............")  
    print("⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣀⣠⣤⣤⣤⣤⣤⣤⣄⣀⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄")
    print("⠄⠄⠄⠄⠄⠄⣀⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣤⣀⠄⠄⠄⠄⠄⠄") 
    print("⠄⠄⠄⠄⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠄⠄⠄⠄")
    print("⠄⠄⠄⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⠄⠄⠄")
    print("⠄⠄⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠄⠄")
    print("⠄⣸⣿⣿⣿⣿⣿⠟⠉⠄⠄⠙⢿⣿⣿⣿⣿⡟⠋⠄⠄⠉⠻⣿⣿⣿⣿⣿⣇⠄")
    print("⠄⣿⣿⣿⣿⣿⣃⣠⣴⣶⣶⣤⡀⣻⣿⣿⣟⢀⣴⣶⣶⣦⣄⢸⣿⣿⣿⣿⣿⠄")
    print("⠄⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠄")
    print("⠄⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠄")
    print("⠄⣿⣿⣿⣿⣿⣿⣿⣿⡏⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⢹⣿⣿⣿⣿⣿⣿⣿⣿⠄")
    print("⠄⣿⣿⣿⣿⣿⣿⣿⣿                ⣿⣿⣿⣿⣿⣿⣿⣿⠄")
    print("⠄⠈⠷⣿⣿⣿⣿⣿⣿                ⣿⣿⣿⣿⣿⣿⣿⠋⠄")
    print("⠄⠄⠄⠄⠙⢿⣿⣿⣿⣿⣶⣤⣉⣉⣉⣉⣉⣉⣤⣶⣿⣿⣿⣿⡿⠋⠄⠄⠄⠄")
    print("⠄⠄⠄⠄⠄⠄⠈⠛⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⠁⠄⠄⠄⠄⠄⠄")
    print("⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠉⠙⠛⠛⠛⠛⠛⠛⠋⠉⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄")

def desenha_forca(tentativas):
    print("  _______     ")
    print(" |/      |    ")

    if(tentativas == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(tentativas == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(tentativas == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(tentativas == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(tentativas == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(tentativas == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (tentativas == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()    

if(__name__ == "__main__"):
    jogar()

