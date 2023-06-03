def palindromo(palavra):
    palavra.upper()
    if palavra == palavra[::-1]:
        return True
    else:
        return False

print(palindromo("radar"))

palavra="Python"
print(palavra[1:len(palavra)-1])
