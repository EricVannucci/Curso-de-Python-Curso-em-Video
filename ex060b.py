from math import factorial

num = int(input('Digite um número para descobir seu fatorial: '))
cont = num
print(f'Calculando o {num}! → ', end='')
while cont != 1:
    print((cont + 1) - 1, 'x', end=' ')
    cont -= 1
print(f'1 = {factorial(num):,}'.replace(',', '.'))
