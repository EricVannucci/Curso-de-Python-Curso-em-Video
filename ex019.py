import random
nome1 = str(input('Nome do primeiro aluno: '))
nome2 = str(input('Nome do segundo aluno: '))
nome3 = str(input('Nome do terceiro aluno: '))
nome4 = str(input('Nome do quarto aluno: '))
lista = [nome1, nome2, nome3, nome4]
print(f'O aluno escolhido foi: {random.choice(lista)}')

print('****Outra forma de fazer o exercício usando parte da biblioteca****')

from random import choice
n1 = str(input('Nome do primeiro aluno: '))
n2 = str(input('Nome do segundo aluno: '))
n3 = str(input('Nome do terceiro aluno: '))
n4 = str(input('Nome do quarto aluno: '))
lista = [n1, n2, n3, n4]
print(f'O aluno escolhido foi: {choice(lista)}')