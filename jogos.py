import adivinhacao
import forca

print("**********************************")
print(".......Escolha o seu jogo!........")
print("**********************************")

print("(1)- Adivinhação")
print("(2)- Forca")

escolha = int(input("Qual jogo? "))

if(escolha == 1):
    print("Você escolheu Adivinhação!")
    adivinhacao.jogar()
elif(escolha == 2):
    print("Você escolheu Forca!")
    forca.jogar()

