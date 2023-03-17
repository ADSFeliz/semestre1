#Crie um programa que informa se o ano atual é par ou ímpar. Para isso, utilize a biblioteca datetime do Python
from datetime import date

data = date.today()

if data.year//2==0:
    print(f"O ano {data.year} é par.")
else:
    print(f"O ano {data.year} é impar.")

