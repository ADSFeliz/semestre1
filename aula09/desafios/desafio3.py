import sys

n1_n2 = input('Número 1 e número 2: ')
numeros = n1_n2.split()
n1,n2= int(numeros[0]),int(numeros[1])
menor_inteiro = -1*sys.maxsize

for n3 in range(n1,menor_inteiro,-1):
    media = (n1+n2+n3)/3
    if(media == n1):
        print(n3)
        break