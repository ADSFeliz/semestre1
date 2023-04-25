precos = {"Banana": 3.80, "Maçã": 4.00, "Melancia": 10.00}

# Quantidade comprada de cada produto
quantidade_compras = {"Banana": 2, "Maçã": 2, "Melancia": 1}

total = 0
for key in precos:
    total += precos[key] * quantidade_compras[key]

print(f"Preço total: R$ {total:.2f}")
