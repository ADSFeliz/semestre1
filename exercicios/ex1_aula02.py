# anoIngresso = 2023
# semestres = 6
# final = anoIngresso + (semestres//2)
# print(f"Ada irá se formar em {final}")

# Realizando o mesmo código com função

def formar(ano, semestres):
    return ano + (semestres//2)

print(f"Ada irá se formar em {formar(2023,6)}")