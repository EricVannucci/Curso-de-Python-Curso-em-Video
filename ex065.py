print('\033[96m  Maior e Menor Valores\033[m')
print('\033[96m~\033[m' * 25)
n = cont = soma = 0
continua = str
maior_menor = []
while continua != 'n':
    n = int(input('Digite um número inteiro: '))
    continua = str(input('Quer continuar? [S/N] ')).strip().lower()
    cont += 1
    soma += n
    maior_menor += [n]
print(f'Você digitou {cont} números, e a média entre eles é {soma/cont}.')
print(f'O maior número digitado foi {max(maior_menor)} e o menor foi {min(maior_menor)}.')
