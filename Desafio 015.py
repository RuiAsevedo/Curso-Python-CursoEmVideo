km = float(input('Quantos km rodou com o carro? '))
dias = int(input('Quantos dias você ficou com o carro? '))
custoDia = dias * 60
custoKm = km * 0.15
total = custoKm + custoDia

print('Você rodou {}km e ficou {} dias com o carro. O total a pagar R$ {:.2f} '.format(km, dias, total))
