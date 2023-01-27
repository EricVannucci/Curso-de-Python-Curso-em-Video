"""Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios e colocar em
uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior
valor que estão na tupla."""

from random import randint

num1 = randint(1, 50)
num2 = randint(1, 50)
num3 = randint(1, 50)
num4 = randint(1, 50)
num5 = randint(1, 50)
sorteio = (num5, num4, num3, num2, num1)

print(f'Os números sorteados são: \n{sorteio}')
print(f'O maior número sorteado foi {max(sorteio)}')
print(f'O menor número sorteado foi {min(sorteio)}')
