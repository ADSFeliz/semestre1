import requests
cep = int(input("Digite o CEP da cidade para saber o nome dela: "))
r = requests.get(f'http://viacep.com.br/ws/{cep}/json/')
dicionario = r.json()

print(dicionario['localidade'])