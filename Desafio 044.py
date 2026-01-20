print('{:=^40}'.format(' LOJA DO CHAVES ='))
valor = float(input('Qual o preço do produto? R$ '))

while True:
    print('''Escolha uma forma de pagamento:
    [1] Dinheiro / Cheque
    [2] à vista no cartão
    [3] Em 2x no cartão
    [4] Em 3x ou mais no cartão''')
    opcao = int(input(' Sua opção: '))

    if opcao == 1:
        print(f'O valor a ser pago com 10% de desconto é de R${valor * 0.90:.2f}')
        break

    elif opcao == 2:
        print(f'O valor a ser pago com 5% de desconto é de R${valor * 0.95:.2f}')
        break

    elif opcao == 3:
        print(f'O valor a ser pago é de R${valor:.2f}')
        break
    elif opcao == 4:
        parcelamento = int(input('Em quantas vezes deseja parcelar? '))

        if parcelamento <3:
            print('Refaça a operação! ')
        elif parcelamento > 12:
            print('Desculpe. Parcelamos em no máximo de 12 vezes. Refaça a operação.')
        else:
            print(f'O valor a ser pago em {parcelamento} vezes, com 20% de juros é de R${valor * 1.20:.2f}')
            break

    else:
        print(f'Opção inválida, tente novamente!')