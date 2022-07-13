print(f'\033[96m{"Par ou Ímpar?":^25}\033[m')
num = int(input('Digite um número qualquer: '))
if num % 2 == 0:
    print(f'O número {num} é \033[96mPAR\033[m')
else:
    print(f'O número {num} é \033[96mÍMPAR\033[m')
