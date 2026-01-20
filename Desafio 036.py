salario = float(input('Por favor, informe sua renda: R$ '))
imovel = float(input('Qual o valor do imóvel a ser financiado? R$ '))
prazo = 12 * float(input('Quantos anos deseja pagar: '))
margem = salario * (30/100)

financiamento = imovel / prazo
print(f'O valor da parcela do imóvel é R${financiamento:.2f}')

if financiamento < margem:
    print(f'Sua margem é de R${margem:.2f}. Parabéns, o finaciamento será aprovado!')
elif financiamento == margem:
    print(f'Vai ficar apertado mas com a margem de R${margem:.2f}. É possivel o finaciamento')
else:
    financiamento > margem
    print(f'Desculpe, mas sua margem é de R${margem:.2f}, por isso não sera aprovado!')