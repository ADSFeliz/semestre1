def andar(comando,x,y,direcao):
    letras=comando.lower()
    direcao=direcao.lower()
    letras=list(letras)
    for i in letras:
        if(i=="a"):
            if(direcao=="norte" or direcao=="sul"):
                if direcao=="norte":
                    y+=1
                else:
                    y-=1
            if(direcao=="leste" or direcao=="oeste"):
                if direcao=="leste":
                    x+=1
                else:
                    x-=1
        elif(i=="r" and direcao=="norte") or \
            (i=="l" and direcao=="sul"):
            direcao="leste"
        elif(i=="r" and direcao=="sul") or \
            (i=="l" and direcao=="norte"):
            direcao="oeste"
        elif(i=="r" and direcao=="leste") or \
            (i=="l" and direcao=="oeste"):
            direcao="sul"
        elif(i=="r" and direcao=="oeste") or \
            (i=="l" and direcao=="leste"):
            direcao="norte"
    return x,y,direcao

x_inicial,y_inicial=7,3
direcao_inicial = "norte"
comando="RAALAL"

x,y,direcao=andar(comando,x_inicial,y_inicial,direcao_inicial)

print(f"As cordenadas são ({x},{y}) e sua direção é {direcao}.")