alunos=0
notas=0
while True:
    escolha=input(f"Digite a nota do aluno {alunos} ou digite SAIR para calcular a média: ")
    if escolha.lower() == "sair":
        if alunos==0:
            print("Sem notas")
            break  
        else:
            media = notas/alunos
            print(f"A média da turma é {media:.2f}")
            break  
        
    notas+=float(escolha)
    alunos+=1 