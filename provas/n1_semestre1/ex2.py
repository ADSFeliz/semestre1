def quemVenceu(n1,n2):
    if n1==n2:
        return 0
    elif n1>n2:
        return 1
    else:
        return 2

time1=int(input("Digite os gols do primeiro time: "))
time2=int(input("Digite os gols do segundo time: "))

print(quemVenceu(time1,time2))