def direcao(dir1,dir2):
    if dir1 == dir2:
        return 0
    if dir1 == "leste" or dir1 == "oeste":
        if dir2 == "norte" or dir2 == "sul":
           return 90
        if dir2 == "leste" or dir2 == "oeste":
            return 180
    if dir1 == "sul" or dir1 == "norte":
        if dir2 == "oeste" or dir2 == "leste":
           return 90
        if dir2 == "sul" or dir2 == "norte":
            return 180
       
cord1_cord2 = input('Ponto inicial e ponto final: ')
cordenadas = cord1_cord2.split()
cord1,cord2= cordenadas[0],cordenadas[1]

print(direcao(cord1,cord2))
