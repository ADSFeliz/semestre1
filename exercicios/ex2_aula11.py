# Faça um programa que simule um lançamento de dados. Lance o dado 100 vezes e armazene 
# os resultados em um array. Depois, mostre quantas vezes cada valor foi conseguido. 
# Dica: use um array de contadores (1-6) e uma função para gerar números aleatórios, 
# simulando os lançamentos dos dados.
import random;

numero=[0,0,0,0,0,0]
for i in range(0,100):
    jogada = random.randint(1,6)
    numero[jogada-1]+=1

for n in range(0,6):
    print(f"Teve {numero[n]} jogadas com o número {n+1}.")
