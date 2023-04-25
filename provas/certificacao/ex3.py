def is_isogram(palavra):
    letras_vistas = {}
    for letra in palavra.lower():
        if letra in letras_vistas:
            return False
        else:
            letras_vistas[letra] = True
    return True

print(is_isogram("machine")) # True
print(is_isogram("isogram")) # True
print(is_isogram("AbCdefg")) # True (lembrando que está convertendo todas as letras para minúsculas)
print(is_isogram("11letters")) # False
print(is_isogram("hello world!")) # False