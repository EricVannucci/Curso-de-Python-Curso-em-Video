from math import factorial

num = int(input('Digite um número inteiro para descobrir seu fatorial: '))
for c in range(num, 1, -1):
    print(c, 'x', end=' ')
print(f'1 = {factorial(num):,}'.replace(',', '.'))
