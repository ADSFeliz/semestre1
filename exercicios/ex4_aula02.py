pessoas = int(input("Digite quantas pessoas irão: "))
pedacos = int(input("Digite quantos pedaços comem em média: "))
totalPedacos = pessoas * pedacos
pizza = 12

if(totalPedacos%12 == 1):
    pizzas = totalPedacos//12 + 1
    print(f"Irão precisar comprar {pizzas} pizzas.")
else:
    pizzas = totalPedacos//12
    print(f"Irão precisar comprar {pizzas} pizzas.")

pizzas = totalPedacos/12
print(f"Cada pessoa irá comer {pizzas:.2f} pedaços de pizza")
