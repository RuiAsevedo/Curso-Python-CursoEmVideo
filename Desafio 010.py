real = float(input('Quantos reais você tem?R$ '))
dolar = real / 5.33

print('Com R${:.2f}, você pode comprar U$${:.2f}' .format(real, dolar))
