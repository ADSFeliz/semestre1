import random

# Definindo as cores em variaveis. Realizado uma pesquisa para não precisar importar uma função de cor
JG1 = '\033[92m' #VERDE
JG2 = '\033[93m' #AMARELO
RESET = '\033[0m' #RESETAR COR

def jogar(jogada_jogador_1, jogada_jogador_2): # Função para definir o resultado de cada partida
    if jogada_jogador_1 == jogada_jogador_2:
        return "Empate", 0
    #Realizado a verificação de todas as jogadas do Jogador 1 em um IF para economizar
    elif (jogada_jogador_1 == 1 and jogada_jogador_2 == 3) or \
         (jogada_jogador_1 == 2 and jogada_jogador_2 == 1) or \
         (jogada_jogador_1 == 3 and jogada_jogador_2 == 2):
        return "Resultado partida: Jogador 1", 1 #Usando um retorno em tuplas para com uma string e Int (x,y)
    else:
        return "Resultado partida: Jogador 2", 2

def resultadoJogo(pontos_jogador_1, pontos_jogador_2): #Função para definir quem ganhou após a soma dos pontos das 3 partidas
    if pontos_jogador_1 > pontos_jogador_2:
        return JG1 + "Resultado melhor de três: Jogador 1" + RESET #Cores definidas nas variaveis ali em cima. 
    elif pontos_jogador_2 > pontos_jogador_1:
        return JG2 + "Resultado melhor de três: Jogador 2" + RESET
    else:
        return "Resultado melhor de três: Empate"

pontos_jogador_1, pontos_jogador_2 = 0, 0 #Variaveis em tuplas para guardar o valor do melhor de três
cont = 0
while cont < 3: #Uma repetição com condição, irá repetir até o cont ser maior que 3
    jogada_jogador_1 = int(input("Informe a sua jogada: (1) Pedra (2) Papel (3) Tesoura: "))
    jogada_jogador_2 = random.randint(1, 3)#Importada função random para escolher número aleatório
    
    resultado, ponto = jogar(jogada_jogador_1, jogada_jogador_2) # como o return da função foi em tuplas, para salvar tbm precisa ser
    print(resultado)# Primeiro valor da tupla onde apresenta o resultado da rodada
    pontos1, pontos2 = 0, 0 #Variaveis em tuplas
    if ponto == 1: # Verificação do segundo valor da tupla que defini para quem vai o ponto da rodada
        pontos_jogador_1 += 1 # acrescenta mais 1 no valor original
    elif ponto == 2:
        pontos_jogador_2 += 1
    cont += 1 #realiza o aumento do cont para o while não ficar infinito

print(resultadoJogo(pontos_jogador_1, pontos_jogador_2)) #Chama a função para definir o ganhador do melhor de três