import sys

menor=sys.maxsize
maior = sys.maxsize*-1
soma = 0 
for i in range(1, 11):
    number = int(input(f'Digite a idade da {i}° pessoa: ')) 
    if number<menor:
        menor=number
    if number>maior:
        maior=number
    soma+=number
    
print(f"A idade maior é {maior}")
print(f"A idade menor é {menor}")
print(f'A média de idade é {soma/10}')