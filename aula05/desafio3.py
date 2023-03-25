def alvo(x,y):
    if (x>=-1 and y<1) and \
       (y>-1 and x<1):
        return "Tu é foda, ganhou 10 pontos"
    elif (x>-5 and y<5) and \
         (y>-5 and x<5):
        return "Está quase lá, 5 pontos"
    elif (x>-10 and y<10) and \
         (y>-10 and x<10):
        return "Você pode melhorar, 1 ponto"
    else:
        return "Errou o alvo"

x,y=10,0
print(alvo(x,y))