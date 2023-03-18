# Exercicio para descobrir o intervalo de um número.
def periodo(n):
    if n>=0 and n <=25:
        return "[0,25]"
    elif n>25 and n<=50:
        return "(25,50]"
    elif n>50 and n<=75:
        return "(50,75]"
    elif n>75 and n<=100:
        return "(75,100]"
    else:
        return "Fora de intervalo"

print(periodo(25.000000000000001))
