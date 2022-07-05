print('\033[1;31mAnalisador de números!\033[m')
num1 = int(input('Digite um número inteiro: '))
num2 = int(input('Digite outro número inteiro: '))
if num1 < num2:
    print(f'{num1} é menor que {num2}')
elif num1 > num2:
    print(f'{num1} é maior que {num2}')
else:
    print(f'{num1} e {num2} são iguais!')
