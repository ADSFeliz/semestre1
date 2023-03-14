pessoas = int(input("Digite quantas pessoas irão: "))
pedacos = int(input("Digite quantos pedaços comem em média: "))
totalPedacos = pessoas * pedacos
fatias = 12

pizzas = totalPedacos/fatias
print(f"Será será necessário {round(pizzas, 0)} pizza(s).")
print(f"Cada pessoa irá comer {pedacos:.2f} pedaços de pizza.")