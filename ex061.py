print(20 * '=-')
print(f'\033[96m{"Termos de uma PA":^40}\033[m')
print(20 * '-=')
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
pa = int(input('Quantos termos você deseja? '))
cont = 1
termo = primeiro
while cont <= pa:
    print(f'{termo} → ', end='')
    termo += razao
    cont += 1
print('FIM!')
