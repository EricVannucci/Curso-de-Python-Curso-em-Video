print('-=-=-=-=-=-=-=-=-=-=-=-=')
print('Analisador de triângulos')
print('-='*12)
r1 = float(input('Digite o valor do primeiro seguimento: '))
r2 = float(input('Digite o valor do segundo seguimento: '))
r3 = float(input('Digite o valor do terceiro seguimento: '))
if r1 < r2 + r3 and r2 < r3 + r1 and r3 < r1 + r2:
    print('Esses seguimentos podem formar um triângulo!')
else:
    print('Esses seguimentos NÃO podem formar um triângulo...')
