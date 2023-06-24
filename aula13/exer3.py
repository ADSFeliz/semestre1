dados = {}
while True:
    escolha = input("Vamos criar o seu cadastro, S/N?. ")
    if escolha.lower() == "n":
        break
    cpf = input("Digite o seu CPF: ")
    nome = input("Digite o seu nome: ")
    idade = int(input("Digite o seu idade: "))
    telefone = input("Digite o seu telefone: ")
    dados[cpf] = {"cpf": cpf, "nome": nome, "idade" : idade, "telefone" :telefone}
    
    