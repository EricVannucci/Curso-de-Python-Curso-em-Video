print('='*40)
print(f'{"10 TERMOS DE UMA PA":^40}')
print('='*40)
termo = int(input('Primeiro Termo: '))
razão = int(input('Razão: '))
for c in range(termo, (termo + 10 * razão), razão):
    print(c, end=' → ')
print('Acabou')
