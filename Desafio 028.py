from random import randint

numeroAle = randint(0,5)
usuario = int(input('Escolha um numero entre 0 e 5: '))
print(f'O numero aleatório foi: {numeroAle}, você escolheu o numero: {usuario}')
print(' ')
if usuario == numeroAle:
    print('Parabéns, você certou! ')
else:
    print('Desta vez você não teve sorte! Tente novamente.')
print('-'*10, 'Fim do jogo','-'*10)