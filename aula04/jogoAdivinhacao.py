#Criei um jogo de adivinhação para o aprendizado dos desvios condicionais

import random
 
chute = int(input("Digite um número para adivinhar: "))
numero = random.randint(0,10)
if chute == numero:
    print("Venceu!")
else:
    print("Errou!")
