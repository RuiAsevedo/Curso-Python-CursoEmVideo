numero =  int(input('Digite um numero inteiro: '))
opcao =  str(input('Qual a base de conversão, Binario, Octal ou Hexadecimal? ')).strip().upper()

BINARIO= bin(numero)
OCTAL = oct(numero)
HEXADECIMAL = hex(numero)

if opcao == 'BINARIO':
    print(f'A conversão é {BINARIO[2:]}')

elif opcao == 'OCTAL':
    print(f'A conversão para Octal é {OCTAL[2:]}')

elif opcao == 'HEXADECIMAL':
    print(f'Para Hexadecimal é {HEXADECIMAL[2:]}')

else:
    print('Opção invalida! Tente novamente. ')

print('---FIM---')