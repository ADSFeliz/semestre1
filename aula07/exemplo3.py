# Faça um programa que a partir de um
# valor inteiro informado pelo usuário 
# imprima a sua tabuada até 10.

valor = int(input("Digite um valor inteiro para saber a tabuada: "))
cont=0
while cont<=10:
    soma = valor*cont
    print(f"{cont} X {valor} = {soma}")
    cont+=1