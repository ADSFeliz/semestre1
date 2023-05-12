import sys

n = int(input('Mercados: '))
lista = []
mais_barato = sys.maxsize
for market in range(0, n):
    produto = input('Preço e Peso: ')
    preco_peso = produto.split()
    preco_kg = (1000/int(preco_peso[1]))*float(preco_peso[0])
    mais_barato=min(preco_kg, mais_barato) 
print(f"{mais_barato:.2f}")
