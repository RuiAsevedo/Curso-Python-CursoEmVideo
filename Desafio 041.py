#Progrma de Classificação de Atletas
from datetime import date

anoNasc = int(input("Digite o ano de nascimento: "))
anoAtual = int(date.today().year)

idade = anoAtual - anoNasc

if idade <= 9:
    print(f'O atleta tem {idade} anos. Sua categoria é a Mirim.')
elif idade <= 14:
    print(f'O atleta tem {idade} anos. Participara da categoria Infantil. ')
elif idade <= 19:
    print(f'O atleta tem {idade} anos. Participara da categoria Junior. ')
elif idade == 20:
    print(f'O atleta tem {idade} anos. Participara da categoria Senior. ')
else:
    print(f'O atleta esta na categoria Master. ')

print('*** Fim ***')