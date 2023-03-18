import random

class bcolors:
    JG1 = '\033[92m' #VERDE
    JG2 = '\033[93m' #AMARELO
    RESET = '\033[0m' #RESETAR COR

def jogar(jogada_jogador_1, jogada_jogador_2):
    if jogada_jogador_1 == jogada_jogador_2:
        return "Empate", 0
    elif (jogada_jogador_1 == 1 and jogada_jogador_2 == 3) or \
         (jogada_jogador_1 == 2 and jogada_jogador_2 == 1) or \
         (jogada_jogador_1 == 3 and jogada_jogador_2 == 2):
        return "Resultado partida: Jogador 1", 1
    else:
        return "Resultado partida: Jogador 2", 2

def resultadoJogo(pontos_jogador_1, pontos_jogador_2):
    if pontos_jogador_1 > pontos_jogador_2:
        return bcolors.JG1 + "Resultado melhor de três: Jogador 1" + bcolors.RESET
    elif pontos_jogador_2 > pontos_jogador_1:
        return bcolors.JG2 + "Resultado melhor de três: Jogador 2" + bcolors.RESET
    else:
        return "Resultado melhor de três: Empate"

pontos_jogador_1, pontos_jogador_2 = 0, 0
cont = 0
while cont < 3: 
    jogada_jogador_1 = int(input("Informe a sua jogada: (1) Pedra (2) Papel (3) Tesoura: "))
    jogada_jogador_2 = random.randint(1, 3)
    
    resultado, ponto = jogar(jogada_jogador_1, jogada_jogador_2)
    print(resultado)
    pontos1, pontos2 = 0, 0
    if ponto == 1:
        pontos_jogador_1 += 1
    elif ponto == 2:
        pontos_jogador_2 += 1
    cont += 1

print(resultadoJogo(pontos_jogador_1, pontos_jogador_2))