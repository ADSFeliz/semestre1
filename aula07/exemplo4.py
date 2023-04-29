# O serviço de meteorologia do município contratou você 
# para desenvolver um programa que calcule a 
# temperatura média de uma semana (7 dias) e 
# informe qual foi a maior e a menor temperatura.

cont=1
soma=0
maior=-999999
menor=99999999
while cont<=7:
    temp=float(input(f"Digite a temperatura do dia {cont}: "))
    soma+=temp
    if temp>maior:
        maior=temp
    if temp<menor:
        menor=temp
    cont+=1
    
    
media = soma/7
print(f"A média de temperatura é: {media:.2f} C°")
print(f"A maior temperatura é: {maior:.2f} C°")
print(f"A menor temperatura é: {menor:.2f} C°")