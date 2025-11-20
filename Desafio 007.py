n1 = float(input('Qual a primeira nota? '))
n2 = float(input('Qual a segunda nota? '))
n3 = float(input('Qual a terceira nota? '))
n4 = float(input('Qual a quarta nota?' ))
nf = (n1 + n2 + n3 + n4) / 4

print('Sua nota final é {:.2f}'.format(nf))
if nf >= 6:
        print('Você está aprovado! ')
else:
        print('Você foi reprovado! ')