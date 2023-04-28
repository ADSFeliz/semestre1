import random
numeroSorteado = random.randint(0,20)
jogadas = 0
venceu = False
while jogadas !=3 and venceu == False:
  jogada = int(input(f'Informe a jogada {jogadas}:'))
  if jogada == numeroSorteado:
    print("Você venceu, parabéns!")
    venceu = True
  else:
    jogadas+=1
if venceu == False:
  print(f'Você perdeu! O número sorteado foi {numeroSorteado}')
