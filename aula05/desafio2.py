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
        elif(i=="r"):
            if direcao=="norte":
                direcao="leste"
            elif direcao=="sul":
                direcao="oeste"
            elif direcao=="leste":
                direcao="sul"
            elif direcao=="oeste":
                direcao="norte"
        elif(i=="l"):
            if direcao=="norte":
                direcao="oeste"
            elif direcao=="sul":
                direcao="leste"
            elif direcao=="leste":
                direcao="norte"
            elif direcao=="oeste":
                direcao="sul"
    return x,y,direcao

x_inicial,y_inicial=7,3
direcao_inicial = "norte"
comando="RAALAL"

x,y,direcao=andar(comando,x_inicial,y_inicial,direcao_inicial)

print(f"As cordenadas são ({x},{y}) e sua direção é {direcao}.")