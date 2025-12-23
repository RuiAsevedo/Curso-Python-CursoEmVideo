cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'amarelo': '\033[33m',
         'verde': '\033[32m',
         'pretoebranco': '\033[7;30m',
         'vermelhoSub': '\033[4;31m',
         'vermelho': '\033[31m'}

print(f"{cores['pretoebranco']}'-=' *20, var = cores['limpa']")
print(f"{cores['verde']}ANALISADOR DE TRIANGULO{cores['limpa']}")
print(f"{cores['pretoebranco']}-='*20{cores['limpa']}")

r1 = float(input('Digite o primeiro valor: '))
r2 = float(input('Digite o segundo valor: '))
r3 = float(input('Digite o terceiro valor: '))
if r1 < r2 + r3 and r2 < r3+ r1 and r3 < r1 + r2:
    print(f"{cores['azul']}Os valores acima formam um triangulo {cores['limpa']}")
else:
    print(f"{'vermelho'}Com os segmentos acima, não foi possivel formar um triangulo{cores['limpa']}")