# A Lanchonete do Bairro precisa de um software para controlar o fluxo do caixa diário. 
# Para isso, pediu que você criasse um programa que permite calcular qual foi o lucro do dia. 
# O programa consiste em informar ao final do dia quantos de cada sabor de pastel foram vendidos e 
# calcular o valor total arrecadado descontados os valores para confecção do pastel.

precosVenda = {"Frango": 8.00, "Pastel": 7.00, "Legumes": 6.50}
precoCusto = {"Frango": 2.50, "Pastel": 1.50, "Legumes": 2.00}

frango = int(input("Digite a quantidade de pastéis de frango que foram vendidos: "))
carne= int(input("Digite a quantidade de pastéis de carne que foram vendidos: "))
legumes = int(input("Digite a quantidade de pastéis de legumes que foram vendidos: "))

total = 0

for item in precosVenda:
    total+=precosVenda[item]-precoCusto[item]

print(f"Você vendeu {frango} pastéis de frango. \n Você vendeu {carne} pastéis de carne. \n Você vendeu {legumes} pastéis de legumes. \n O seu lucro é R$ {total:.2f}")