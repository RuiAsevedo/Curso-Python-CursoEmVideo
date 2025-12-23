frase = str(input('Digite uma frase: ')).upper().strip()
print(frase)

quant = frase.count('A')
pri = frase.find('A')+1
ultima = frase.rfind('A')+1

print(f'A letra (A) apareceu {quant} vezes!')
print(f'Apareceu a primeira vez na posição {pri}.')
print(f'E a ultima vez que a letra (A) apareceu na posição {ultima}')