anoIngresso = int(input("Digite o seu ano de ingresso: "))
semestres = int(input("Digite a quantidade de semestres do curso: "))
final=0
if((semestres%2) == 1):
    final = anoIngresso + (semestres//2 + 1)
    print(f"Ada irá se formar em {final}")
else:
    final = anoIngresso + (semestres//2)
    print(f"Ada irá se formar em {final}")