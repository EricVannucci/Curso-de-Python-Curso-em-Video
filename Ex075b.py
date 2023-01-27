"""Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado
e guarde-os em uma tupla. No final, mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares."""
numeros_pares = []
pares = 0
numeros = (int(input('Digite um número: ')), int(input('Digite outro número: ')),
           int(input('Digite mais um número: ')), int(input('Digite um último número: ')))
print(f'Os números escolhidos foram {numeros}')
if 9 not in numeros:
    print('Não foi digitado nenhum número 9.')
else:
    print(f'O número 9 foi digitado {numeros.count(9)} vezes.')
if 3 not in numeros:
    print('Não foi digitado nenhum número 3.')
else:
    print(f'O primeiro número 3 digitado apareceu na posição {numeros.index(3)+1}.')
for n in numeros:
    if n % 2 == 0:
        pares += 1
        numeros_pares.append(n)
print(f'Foram digitados {pares} números pares e eles foram: {numeros_pares}')
