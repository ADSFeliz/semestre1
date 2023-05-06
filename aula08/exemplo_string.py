#O FOR percorre listas. Tanto faz se é uma string ou lista de números. Segue um exemplo com string
def conta_vogais(nome):
        vogais=0
        for letra in nome.lower():
            if letra in "aeiou":
                vogais+=1
        return vogais
palavra = input("Digite uma palavra para ver a quantidade de vogais: ")
print(f"Quantidade de vogais é igual a {conta_vogais(palavra)}")
                