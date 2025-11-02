preço = float(input('Qual o preço produto? R$ '))
desc = preço - (preço * 0.05)

print('O preço do produto é R${:.2f}, aplicado o desconto de 5%, o mesmo saíra por R${:.2f}'.format( preço, desc))
