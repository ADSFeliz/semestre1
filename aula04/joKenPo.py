import random
class bcolors:
    JG1 = '\033[92m' #GREEN
    JG2 = '\033[93m' #YELLOW
    RESET = '\033[0m' #RESET COLOR


pontosJg1,pontosJg2=0,0
pedra, papel, tesoura = 1,2,3

cont = 0
while cont<3:  
    jg1 = int(input("Informe a sua jogada: (1) Pedra (2) Papel (3) Tesoura: "))
    jg2 = random.randint(1,3)

    cont+=1
    if(jg1==jg2):
        print("Empate")
    if jg1==pedra:
        if jg2==papel:
            print("jg2 Venceu")   
            pontosJg2+=1         
        else:
            print("jg1 Venceu")
            pontosJg1+=1       
    if jg1==papel:
        if jg2==pedra:
            print("jg1 Venceu")
            pontosJg1+=1
        else:
            print("jg2 Venceu")
            pontosJg2+=1
    if jg1==tesoura:
        if jg2==papel:
            print("jg1 Venceu")
            pontosJg1+=1
        elif jg2==pedra:
            print("jg2 Venceu")
            pontosJg2+=1

if pontosJg1>pontosJg2:
    print(bcolors.JG1 + "jg1 Venceu melhor de três!" + bcolors.RESET)
elif pontosJg2>pontosJg1:  
    print(bcolors.JG2 + "jg2 Venceu melhor de três!" + bcolors.RESET)
else:
    print("Empatou melhor de três!" )