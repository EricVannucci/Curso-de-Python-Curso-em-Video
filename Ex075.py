"""Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado
e guarde-os em uma tupla. No final, mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares."""

numeros = (int(input('Escreva um número: ')), int(input('Escreva mais um número: ')),
           int(input('Escreva mais um número: ')), int(input('Escreva o último número: ')))
print(f'Os números escolhidos são:')
print(numeros)
if 9 not in numeros:
    print('Não existem números 9.')
else:
    print(f'Apareceram {numeros.count(9)} números nove.')
if 3 not in numeros:
    print('Não existem números 3.')
else:
    print(f'O primeiro número 3 foi encontrado na posição {numeros.index(3)+1}')
print(f'Os números pares são: ', end='')
for n in numeros:
    if n % 2 == 0:
        print(n, end=' ')
