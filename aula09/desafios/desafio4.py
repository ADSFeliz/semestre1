mais_novo = 0
for idade in range(1,3):
    res = int(input(f'Digite a idade do {idade}° irmão: '))
    if idade==1:
        mais_novo+=res

razao = res - mais_novo
print(res+razao)        
