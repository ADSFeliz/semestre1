def ingresso(n1,n2):
    
    if n1<17 and n2<=17:
        return 30
    elif (n1>=18 and n1<60) and (n2>=18 and n2<60):
        return 60
    elif n1>60 and n2>60:
        return 40
    elif(n1<17 and n2>60) or(n1>60 and n2<17):
        return 35
    elif((n1>=18 and n1<60)and n2>60) or (n1>60 and (n2>=18 and n2<60)):
        return 50
    else:
        return 45

idade1=int(input("Digite a sua idade: "))
idade2=int(input("Digite a idade da sua amiga: "))

print(f"{ingresso(idade1,idade2):.2f}")