num = int(input('Digite um número para saber se ele é primo: '))
cont = 0

for c in range(1, num + 1):
    if num % c == 0 and num % 1 == 0:
        print(f'\033[33m{c}\033[m', end=' ')
        cont = cont + 1
    else:
        print(c, end=' ')

if cont == 2:
    print(f'\nO número {num} é PRIMO')
else:
    print(f'\nO número {num} não é PRIMO')
