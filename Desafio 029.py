velocidade =  float(input('Qual a velocidade do carro? '))

if velocidade > 80:
    multa = (velocidade - 80) * 7
    print('Você foi multado e terá de pagar R${:.2f} para o Detran da sua cidade!'.format(multa))
else:
    print('Você esta dentro da velocidade permitida {:.0f} Km/h'.format(velocidade))

print('Em caso de duvidas, contate-nos via central de atendimento: 08003124512')