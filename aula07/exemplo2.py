# Faça um programa que solicite um valor 
# para o usuário e imprima a soma de seus antecessores, 
# a partir de 0, até ele, inclusive.

valor = int(input("Digite um valor inteiro: "))
soma=0
cont=0
while cont<=valor:
    soma+=cont
    print(soma)
    cont+=1