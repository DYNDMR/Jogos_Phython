import random


def jogar():


    print("**********************************")
    print("Bem vindos ao jogo de adivinhações")
    print("**********************************")
    Numero_Secreto = random.randrange(1, 101)
    total_de_tentativas = 0
    pontos = 1000

    print("Escolha o nível de dificuldade:")
    print("(1)-Fácil")
    print("(2)-Médio")
    print("(3)-Difícil")

    nivel = int(input("Defina o nível: "))

    if (nivel == 1):
        total_de_tentativas = 20
    elif (nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    print("Você tem {} pontos".format(pontos))

    # print(Numero_Secreto)
    for rodada in range(1, total_de_tentativas + 1):
        print("tentativa {} de {}". format(rodada, total_de_tentativas))
        chute_str = input("Digite um número de 1 a 100: ")
        print("Você digitou o número:", chute_str)
        chute = int(chute_str)

        if (chute < 1 or chute > 100):
            print("Você deve digitar um número de 1 a 100")
            continue

        acertou = Numero_Secreto == chute
        maior = Numero_Secreto < chute
        menor = Numero_Secreto > chute

        if acertou:
            print("Você acertou! e fez {} pontos".format(pontos))
            break
        else:
            if maior:
                print("você errou :( Esse valor é maior")

            elif menor:
                print("você errou :( Esse valor é menor")

                pontos_perdidos = abs(Numero_Secreto - chute)
                pontos = pontos - pontos_perdidos
                print("Seus pontos agora são: ", pontos)
            
        rodada += 1



    print("``````````````````````````````````")
    print("__________fim de jogo!____________")
    print("..................................")

if(__name__ == "__main__"):
    jogar()

