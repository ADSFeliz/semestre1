# aprendendo funções, deixando o programa reaproveitavel futuramente

def saudacao(nome):# se for necessario passar alguma informação externa para a função inserir dentro dos (), não é obrigátorio
    print("Olá, Mundo!")# Aqui não é necessario nenhuma informação externa
    print(f"Olá, {nome}!")

saudacao("Python")
saudacao("PHP")
saudacao("JAVA")

x = input("Informe o seu nome: ")
saudacao(x)