print(19*'\033[31m=-\033[m')
print('\033[1mAnalisador de empréstimos imobiliários\033[m')
print(19*'\033[31m-=\033[m')
casa = float(input('Digite o valor da casa pretendida R$: '))
salario = float(input('Digite seu salário R$: '))
anos = int(input('Digite o tempo, em anos, desejado para quitação da casa: '))
prest = casa / (anos*12)
print(f'A prestação para casa desejada será de R$ {prest:.2f}')
if prest > (salario * 30/100):
    print('Infelizmente seu salário não é suficiente para esta casa, a parcela excede 30%.')
else:
    print('Você poderá financiar a casa, parabéns!')
