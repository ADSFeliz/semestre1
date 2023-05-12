wins = 0
for jogo in range(0,6):
    res = input('Resultado: ')
    if res.lower() == 'v':
        wins += 1
if wins == 0:
    print(-1)
elif 1 <= wins <= 2:
    print(3)
elif 3 <= wins <= 4:
    print(2)
elif 5 <= wins <= 6:
    print(1)
        