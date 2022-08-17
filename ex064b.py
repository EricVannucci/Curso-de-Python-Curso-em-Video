print('*' * 30)
print('\033[91m Tratando vários valores v1.1\033[m')
print('*' * 30)
n = cont = soma = 0
n = int(input('Digite um número [999 para parar]: '))
while n != 999:
    cont += 1
    soma += n
    n = int(input('Digite um número [999 para parar]: '))
print(f'Você digitou {cont} números e a soma deles é {soma}.')
