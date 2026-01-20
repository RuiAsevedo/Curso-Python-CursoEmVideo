from random import randint
from time import sleep


itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)

print(''' Escolha uma opção: 
    [0] Pedra
    [1] Papel
    [2] Tesoura ''')
jogador = int(input('Qual é sua escolha? '))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')

print('-=' * 11)
print(f'Computador jogou {itens[computador]}')
print(f'Jogador jogou {itens[jogador]}')
print('-=' * 11)

# LÓGICA DE COMPARAÇÃO:
if computador == 0: # Computador jogou PEDRA
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')

elif computador == 1: # Computador jogou PAPEL
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')

elif computador == 2: # Computador jogou TESOURA
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE')
else:
    print('Opção invalida')