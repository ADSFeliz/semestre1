# Desenvolva uma versão simplificada do jogo de cartas “21”. 
# O jogo deve ser jogado por 1 jogador humano e o computador. As regras são:
# O jogador e o computador recebem, alternadamente, 
# cartas com valor entre 1 e 4, podendo estas se repetirem.
# Vence quem somar 21 pontos.
# Perde quem ultrapassar 21 pontos.

import random

pessoa=0
computador=0

while True:
    pessoa+=random.randint(1,4)
    computador+=random.randint(1,4)
    if pessoa == 21 or computador > 21:
        print("O humano venceu!")
        break
    elif pessoa > 21 or computador == 21:
        print("O computador venceu!")
        break

    