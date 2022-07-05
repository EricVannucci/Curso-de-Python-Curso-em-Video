n = int(input('Digite um número: '))
d = n*2
t = n*3
r = n**(1/2)
print('O dobro do número escolhido é {}'.format(d))
print('O triplo do número escolhido é {}'.format(t))
print('A raiz quadrada do número escolhido é {:.2f}'.format(r))

print('** outra forma de fazer com menos variáveis **')

print(f'O dobro de {n} é {n*2}')
print(f'O triplo de {n} é {n*3}')
print(f'A raiz quadrada de {n} é {n**(1/2):.2f}')
