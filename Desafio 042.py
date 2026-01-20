r1 = float(input('Digite o primeiro valor: '))
r2 = float(input('Digite o segundo valor: '))
r3 = float(input('Digite o terceiro valor: '))

if r1 < r2 + r3 and r2 < r3 + r1 and r3 < r1 + r2:
    print(f"Os valores acima formam um triangulo ")
    if r1 == r2 == r3:
        print(f"Os valores acima formam um triangulo Equilátero! ", end= '' )
    elif r1 != r2 != r3 != r1:
        print('Escaleno! ')
    elif r1 == r2 != r3 != r1:
        print('Isoceles! ')
else:
    print(f"Com os segmentos acima, não foi possivel formar um triangulo")