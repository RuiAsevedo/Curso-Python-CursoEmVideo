salario1 = float(input('Digite o salário do funcionário R$: '))
if salario1 <= 1250:
    novo = salario1 + (salario1 * 15 / 100)

else:
    novo = salario1 + (salario1 * 10 / 100)
print(f'O funcionário que ganhava R${salario1:.2f}, passa a receber R$ {novo:.2f}')