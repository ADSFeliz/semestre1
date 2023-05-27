vogais=0

disciplinas = ["Lógica", "Matemática", "Fundamentos da computação", "Inglês Instrumental", "Português e redação técnica", "Matemática"]
for disciplina in disciplinas:
    if disciplina[0].lower() in "aeiou" or disciplina[-1].lower() in "aeiou":
        vogais+=1
print(f"{vogais} disciplinas começam ou terminam com vogais.")
