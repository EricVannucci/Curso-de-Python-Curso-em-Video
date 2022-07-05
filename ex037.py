print(9*'\033[1;34m=-\033[m')
print('\033[7mConversor de bases\033[m')
print(9*'\033[1;34m=-\033[m')
num = int(input('Digite um número inteiro: '))
print('\033[1;34mEscolha uma base de conversão:\033[m')
print('''[1] Converter para BINÁRIO
[2] Converter para OCTAL
[3] Converter para HEXADECIMAL''')
opção = input('Sua opção: ')
if opção == '1':
    print(f'Convertendo o número {num} para Binário: {bin(num)[2:]}')
elif opção == '2':
    print(f'Convertendo o número {num} para Octal: {oct(num)[2:]}')
elif opção == '3':
    print(f'Convertendo o número {num} para Hexadecimal: {hex(num)[2:]}')
else:
    print('Você não escolheu uma opção válida!')
