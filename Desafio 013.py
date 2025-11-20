salário = float(input('Qual é o salário atual do funcinário? R$'))
novoSalário = salário + (salário * 15/100)

print('O salário do funcionário com o aumento de 15% é de R${:.2f},'.format(novoSalário))
