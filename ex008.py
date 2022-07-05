m = float(input('Digite a medida em metros: '))
c = m*100
mm = m*1000
print('A medida em centímetros corresponde a: {:.0f}'.format(c))
print('A medida em milímetros corresponde a: {:.0f}'.format(mm))

print('****Outra forma de fazer o exercício****')

m = float(input('Digite a medida em metros: '))
print(f'A medida em centímetros corresponde a: {m*100 :.0f}')
print(f'A medida em milímetros corresponde a: {m*1000 :.0f}')
