larg = float(input('Qual a largura da parede? '))
alt = float(input('Qual a altura da parede? '))
area = larg * alt

print('A dimensão da parede é {}m²x{}m², e sua área é {}m²  .'.format(larg, alt, area))
tinta = area / 2

print('Você precisará de {} litros de tinta '.format(tinta))
