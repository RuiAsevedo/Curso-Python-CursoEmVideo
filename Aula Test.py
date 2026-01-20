cores = {'limpa':'\033[m',
         'banco': '\033[30m',
         'vermelho': '\033[31m',
         'verde': '\033[32m',
         'amarelo': '\033[33m',
         'azul': '\033[34m',
         'magenta': '\033[35m',
         "cor": '\033[36m',
         'cinza': '\033[37m', }


Nome = str(input('Digite seu nome: ')).strip().upper()
if ('RUI' in Nome):
    print(f"{cores['azul']}Que nome lindo você tem!{cores['limpa']}")
else:
    print(f"{cores['vermelho']} Seu nome é comum!'{cores['limpa']}")
print(f"{cores['verde']}, Bom dia, {Nome}!{cores['limpa']}")