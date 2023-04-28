# O jogo da adivinhação consiste em um jogador humano ter 3 
# chances para acertar qual número foi sorteado pelo computador entre 0 e 20.

import random

def adivinhar(numero, adivinhar):
    if(numero == adivinhar):
        return True
    else:
        return False

numero = random.randint(0,20)

chute = int(input("Adivinhe um número que o computador sorteou: "))
if(adivinhar(numero,chute)):
    print("Parabéns você acertou!")
else:
    chute = int(input("Adivinhe o número novamente que o computador sorteou: "))
    if(adivinhar(numero,chute)):
        print("Parabéns você acertou!")
    else:
        chute = int(input("Adivinhe o número novamente que o computador sorteou: "))
        if(adivinhar(numero,chute)):
            print("Parabéns você acertou!")
        else: 
            print("Você não acertou nas 3 tentativas")



