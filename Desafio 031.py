distancia = float(input('Usuário, qual a distância de sua viagem em km? '))

if distancia <= 200:
    print('O preço da passagem é R${:.2f}'.format(distancia * 0.50))

else:
    print(f'O preço da passagem é R${distancia * 0.45:.2f}')