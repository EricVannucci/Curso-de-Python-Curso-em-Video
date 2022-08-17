print('~' * 30)
print('\033[96m Tratando vários valores v1.0\033[m')
print('~' * 30)
n = 0
cont = 0
total = 0
while n != 999:
    n = int(input('Digite um número [999 para parar]: '))
    cont += 1
    total += n
print(f'Foram digitados {cont - 1} números e a soma deles é {total - 999}')
