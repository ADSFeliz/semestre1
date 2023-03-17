#Aprendendo as funcionalidades do If, Elif e Else

def aprovacao(n1,n2):
    media = (n1+n2)/2
    if media>=7:
        return "Aprovou"
    elif media>=1.7:
        return "Exame"
    else:
        return "Reprovou"

print(aprovacao(7,9))

