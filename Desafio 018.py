import math

angulo = float(input('Digite o valor do angulo: '))
se = math.sin(math.radians(angulo))
co = math.cos(math.radians(angulo))
tan = math.tan(math.radians(angulo))

print('O valor de Seno é: {:.2f}, do Cosseno é: {:.2f} e da Tangente: {:.2f}'. format(se, co, tan))