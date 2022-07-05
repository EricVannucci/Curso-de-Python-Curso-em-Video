salario = float(input('Digite o salário atual R$ '))
if salario <= 1250:
    novo = (salario * 0.15) + salario
if salario > 1250:
    novo = (salario * 0.10) + salario
print(f'Seu novo salário é: R${novo:.2f}')
