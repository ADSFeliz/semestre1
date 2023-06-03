# Dadas duas cadeias s e t de igual comprimento, a distância de Hamming entre s e t, 
# denotada por dH(s,t), é o número de símbolos correspondentes que diferem em s e t.

def distancia_hamming(s,t):
    diferencas = 0
    for i in range(0,len(s)):
        if t[i] != s[i]:
            diferencas+=1
    return diferencas

cadeia_s = "GAGCCTACTAACGGGA"
cadeia_t = "CATCGTAATGACGGCC"

print(distancia_hamming(cadeia_s,cadeia_t))