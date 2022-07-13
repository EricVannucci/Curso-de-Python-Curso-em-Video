cont = 0
soma = 0
num = int(input('Digite um número para saber se ele é primo: '))
for c in range(1, num + 1):
    print(c, end=' ')
if num // num and num // 1:
    print(f'\nO número {num} é PRIMO')
else:
    print(f'\nO número {num} não é PRIMO')
