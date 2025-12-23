n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
n3 = int(input('Digite o terceiro numero: '))

#menor = min(n1, n2, n3)
#maior = max(n1, n2, n3)
#print(f'O meno numero digitado foi {menor} e o maior foi {maior}.')

menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3

maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3

print(f'O menor valor digitado foi {menor}')
print(f'O maior valor digitado foi {maior}')