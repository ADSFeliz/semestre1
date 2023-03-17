# Faça um jogo em que o computador sorteie um valor entre 1 e 10 e uma pessoa deve adivinhar qual foi o valor sorteado. 
# Adicione após as seguintes regras: 
# Dê duas tentativas para o usuário:
# Informe se o valor é maior ou menor do que o digitado pela pessoa:

import random

tentativas=0
numero = random.randint(0,10)

while tentativas<2:
    chute = int(input("Digite um número para adivinhar: "))
    if chute == numero:
        print("Você venceu!")
        break
    else:
        if numero<chute:
            print("Errou! O número é menor")
            tentativas+=1
        else:   
            print("Errou! O número é maior")
            tentativas+=1
print(f"O número aleatório é {numero}.")