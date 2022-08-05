print('\033[34m=-\033[m' * 12)
print(f'\033[96m{"Gerador de PA":^23}\033[m')
print('\033[34m=-\033[m' * 12)
primeiro = int(input('Qual o primeiro termo: '))
razao = int(input('Qual a razão: '))
termo = primeiro
cont = 1
total = 0
replay = 10
while replay != 0:
    total = total + replay
    while cont <= total:
        print(f'{termo} → ', end='')
        termo += razao
        cont += 1
    print('PAUSA')
    replay = int(input('Quantos termos você quer mostrar a mais? '))
print(f'Fim, foram ao final {total} termos calculados.')
