pessoas = int(input("Digite quantas pessoas irão: "))
pedacos = int(input("Digite quantos pedaços comem em média: "))
totalPedacos = pessoas * pedacos
fatias = 12

if(totalPedacos%12 > 0):
    pizzas = totalPedacos//fatias + 1
    print(f"Irão precisar comprar {pizzas} pizzas.")
else:
    pizzas = totalPedacos//fatias
    print(f"Irão precisar comprar {pizzas} pizzas.")

print(f"Cada pessoa irá comer {pedacos:.2f} pedaços de pizza")
