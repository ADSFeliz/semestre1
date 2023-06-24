from random import randint
faces = {5: 1601, 6: 1734, 2: 1696, 3: 1688, 4: 1633, 1: 1648}
for x in range(0,10000):
    faceSorteada = randint(1,6)
    #A função get retorna um valor padrão para a posição no dicionário
    faces[faceSorteada] = faces.get(faceSorteada,0)+1
print(faces)

#Converte as chaves em uma lista
chaves = list(faces.keys())
#Ordena uma lista
chaves.sort()
#Percorre as chaves ordenadas
for key in chaves:
    print(key,"-",faces[key])
    
#Deletar por chave
del faces[5]
#Remover e retornar por chave
faces.pop(6)
#Remover e retornar item aleatório
faces.popitem()
#Limpar o dicionário
faces.clear()