def triangulo(a,b,c):
    if a==b==c:
        return "É um triangulo equilátero"
    elif (a==b or a==c or b==c):
        return "É um triangulo isósceles"
    else:
        return "É triângulo escaleno"

def ehTriangulo(a,b,c):
    if(a>0 and b>0 and c>0):
        if (a+b>=c) and (b+c>=a) and (a+c>=b):
            return True
        else:
            return False
    else:
        return False

lado1 = 1
lado2 = 1
lado3 = 0
if ehTriangulo(lado1,lado2,lado3):
    print(triangulo(lado1, lado2, lado3))
else:
    print("Não é um triângulo")

