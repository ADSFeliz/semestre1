def calculo(valor):
    for cont in range(0,11):
        res = valor*cont
        print(f"{cont} X {valor} = {res}")

def regressiva():
    for cont in range(5,0,-1):
        print(cont)
        
valor = int(input("Digite um valor inteiro para saber a tabuada: "))
calculo(valor)
regressiva()