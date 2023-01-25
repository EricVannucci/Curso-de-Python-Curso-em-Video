extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete',
           'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze',
           'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
novamente = 's'
while True:
    while novamente not in 'sn':
        print('Opção inválida, digite S para SIM ou N para NÃO.')
        novamente = str(input('Deseja inserir novo número? [S/N]')).lower().strip()
    if novamente == 's':
        numero = int(input('Escolha um número de 0 a 20: '))
        if 0 <= numero <= 20:
            print(f'O número {numero} por extenso é {extenso[numero]}')
        else:
            print('Número inválido, tente novamente!')
        novamente = str(input('Deseja inserir novo número? [S/N]')).lower().strip()
    elif novamente == 'n':
        print('OK, então... tchau!')
        break
