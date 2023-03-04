nome = input("Informe seu nome:")
quantidade = int(input("Informe qual é a quantidade comprada:"))
precoUni = float(input("Informe qual é o preço do produto:"))
precoTotal = quantidade*precoUni # reutilizando variaveis
print(f"{nome} sua compra tem {quantidade} itens e custa R$ {precoUni} por unidade. O valor da compra é: R$ {precoTotal:.2f}")