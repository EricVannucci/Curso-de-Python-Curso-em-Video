print('\033[96m*** Cadastramento de Pessoas ***\033[m')
mais_18 = 0
homens = 0
mulher_menos_20 = 0

while True:
    print('=' * 20)
    print('CADASTRE UMA PESSOA:')
    print('=' * 20)
    nome = str(input('Nome: ')).strip().capitalize()
    idade = int(input('Idade: '))
    if idade >= 18:
        mais_18 += 1
    sexo = ' '
    while sexo not in 'mf':
        sexo = str(input('Sexo [M/F]:  ')).strip().lower()[0]
        if sexo == 'm':
            homens += 1
        elif sexo == 'f' and idade < 20:
            mulher_menos_20 += 1
    continua = ' '
    while continua not in 'sn':
        continua = str(input('Deseja continuar? [S/N]: ')).strip().lower()[0]
    if continua == 'n':
        break
print('Cadastramento encerrado...\n')
print('=-' * 6)
print('Estatísticas')
print('=-' * 6)
if mais_18 == 0:
    print('Não foram cadastrados pessoas com mais de 18 anos.')
else:
    print(f'Total de pessoas com mais de 18 anos: {mais_18}.')
if homens == 0:
    print('Não houveram homens cadastrados.')
else:
    print(f'Ao todo foram cadastrados {homens} homem(ns).')
if mulher_menos_20 == 0:
    print('Não existem mulheres com menos de 20 anos cadastradas.')
else:
    print(f'Foram cadastrada(s) {mulher_menos_20} mulher(es) com menos de 20 anos.')
