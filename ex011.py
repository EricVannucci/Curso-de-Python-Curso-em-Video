print('Digite as medidas da area a ser pintada em metros.')
a = float(input('Altura: '))
l = float(input('Largura: '))
h = (a*l)
m = h**2
print('A área a ser pintada possui {:.2f} metros quadrados'.format(h))
t = h/2
print('Você precisará de {:.2f} litros de tinta para pintar {:.2f} de área informada.'.format(t,h))
print('****Outra forma de fazer o excercício****')
print('Digite as medidas da area a ser pintada em metros: ')
a = float(input('Altura: '))
l = float(input('Largura: '))
h = a*l
m = h/2
print(f'Sua parede tem {h}m² e serão necessários {m} litros de tinta.')