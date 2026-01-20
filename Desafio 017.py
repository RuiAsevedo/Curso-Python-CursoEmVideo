import math

catetoOposto = float(input('Digite o cumprimento do Cateto Oposto: '))
catetoAdjacente = float(input('Digite o cumprimento do Cateto Adijacente: '))

#hipotenusa = (catetoOposto**2 + catetoAdjacente**2) ** (1/2)
#print(f'A Hipotenusa vai medir {hipotenusa:.2f}')

hipotenusa = math.hypot(catetoOposto, catetoAdjacente)
print(f'A Hipotenusa vai medir {hipotenusa:.2f}')