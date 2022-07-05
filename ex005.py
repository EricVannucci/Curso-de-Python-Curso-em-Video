'''Duas formas corretas de fazer, a primeira melhor quando for precisar das
variáveis mais para frente no programa.'''

n1 = int(input('Digite um número: '))
n0 = n1-1
n2 = n1+1

print('O antecessor do número escolhido é {} e o sucessor é {}.'.format(n0, n2))

n = int(input('Digite um número: '))
print(f'Analisando o número {n}, seu antecessor é {(n-1)} e seu sucessor é {(n+1)}')
