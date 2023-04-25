import random

numeros=[]
maiores=[]
menores=[]
soma=0
for i in range(0,100):
    numero = random(0,1000)
    numeros.add(numero)
    soma+=numero

media = soma/(len(numeros))
for i in range(len(numeros)):
    if numeros[i]>media:
        maiores.add(numeros[i])
    if numeros[i]<media:
        menores.add(numeros[i])

print(f"Media: {media} Maiores:{len(maiores)} Menores:{len(menores)}")

