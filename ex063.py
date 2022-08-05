print('Gerador de PA:')
primeiro = int(input('Qual o primeiro termo: '))
razao = int(input('Qual a razão: '))
cont = 1
pa = 0
total = 10
while total != 0:

    while cont <= total:
        print(f'{primeiro} → ', end='')
        primeiro += razao
        cont += 1
print('Pausa')
