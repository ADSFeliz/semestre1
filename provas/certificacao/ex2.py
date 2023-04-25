def converte(valor):
    cotacaoEuro = 0.18
    valorConvertido = cotacaoEuro*valor
    print(f"O valor em euro é: € {valorConvertido:.2f}")

real = float(input("Digite o valor para converter: "))
converte(real)