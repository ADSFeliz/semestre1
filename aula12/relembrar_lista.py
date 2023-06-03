numeros = []
maior=[]
menor=[]
soma=0
for i in range(0,10):
    numeros.append(int(input(f"Digite o {i+1}° número: ")))
for number in numeros:
    soma+=number

quantidade_numbers=len(numeros)
media=soma/quantidade_numbers
print(f"A soma dos {quantidade_numbers} números é {soma} e a média é {media}.")

for number in numeros:
    if number > media:
        maior.append(number)
    else:
        menor.append(number)

print(maior, menor)