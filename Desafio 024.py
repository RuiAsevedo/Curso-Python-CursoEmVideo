cidade = str(input('Digite o nome de sua cidade natal: ')).strip()
print(cidade[0:5].upper() == 'Santo')


#Forma mais precisa de realizar o mesmo programa:
##Verifica se começa com 'SANTO', ignorando maiúsculas/minúsculas na entrada

#cidade = str(input('Em que cidade você nasceu? ')).strip()
#print(cidade.upper().startswith('SANTO'))