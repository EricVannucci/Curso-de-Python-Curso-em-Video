nome = str(input('Digite seu nome completo: ')).strip().lower()
nomes = nome.split()
print('Seu nome tem Silva? {}'.format(nomes.__contains__('silva')))
''' outra forma de resolver '''
print('Seu nome tem Silva? {}'.format('silva' in nomes))
