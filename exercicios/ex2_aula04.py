#O painel de um Microondas possibilita que ao clicar no botão “+30” sejam adicionados 30 segundos 
#ao tempo de uso do aparelho. Porém, o tempo é medido em minutos, 
#de forma que dois cliques no botão resultem em 1 minuto. 
#Assim, pede-se que você crie uma função que ao ser executada adicione 30 segundos ao tempo de uso de um 
#Microondas e exiba o tempo total no formato de minutos.

def microondas(tempo,tempoMicroondas):
    tempoMicroondas=tempoMicroondas*60
    tempoMicroondas+=tempo*30
    return tempoMicroondas/60

print(microondas(2,1))
    
