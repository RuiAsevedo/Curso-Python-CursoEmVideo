from datetime import date

ano_nasc = int(input('Digite o ano do seu nascimento: '))

anoAtual = date.today().year
idade = anoAtual - ano_nasc
saldo = idade - 18
ano_alist = anoAtual - saldo
print('-' * 40)
print(f'Nascidos em {ano_nasc}, em {anoAtual}, tem {idade} anos de idade')
print(' ')

if idade < 18:
    print(f'Você ainda não completou 18 anos, volte daqui a {18 - idade} anos.')

elif idade == 18:

    print('Você precisa se alistar este ano, não deixe pra depois!')

else:
    print(f'Você tem {idade} anos, deveria ter se alistado em {ano_alist}, procure um quartel o quanto antes!')
