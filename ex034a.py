salario = float(input('Digite o salário atual R$ '))
if salario <= 1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)
print(f'O novo salário será de R$ {novo:.2f}')
