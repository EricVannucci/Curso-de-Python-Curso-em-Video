a = str(input('Digite o nome do aluno: '))
n1 = float(input('Digite a primeira nota do aluno: '))
n2 = float(input('Digite a segunda nota do aluno: '))
m = (n1 + n2)/2
print('A média do aluno {} é: {:.1f}.'.format(a, m))

print('***Outra forma de fazer o exercício***')

n = str(input('Digite o nome do aluno: '))
a = float(input('Digite a primeira nota do aluno: '))
b = float(input('Digite a segunda nota do aluno: '))
print(f'A média do aluno {n} é: {(a+b)/2 :.1f}')
