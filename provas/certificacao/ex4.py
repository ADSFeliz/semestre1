import random

numeros=[]
maiores=[]
menores=[]
soma=0
for i in range(0,100):
    numero = random.randint(0,1000)
    numeros.append()(numero)
    soma+=numero

media = soma/(len(numeros))
for i in range(len(numeros)):
    if numeros[i]>media:
        maiores.append(numeros[i])
    if numeros[i]<media:
        menores.append(numeros[i])

print(f"Media: {media} Maiores:{len(maiores)} Menores:{len(menores)}")
