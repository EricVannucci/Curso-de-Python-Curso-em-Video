from num2words import num2words

novamente = 's'
while True:
    while novamente not in 'sn':
        print('\033[33mOpção inválida, tente novamente!\033[m')
        novamente = str(input('Deseja tentar novo número? [S/N]: ')).strip().lower()
    if novamente == 's':
        numero = int(input("Digite um número entre 0 e 100: "))
        if 0 <= numero <= 100:
            num = num2words(numero, lang='pt_br')
            print(f"O numero por extenso é: {num}")
        else:
            print('Número inválido, deve ser entre 0 e 100!')
        novamente = str(input('Deseja tentar novo número? [S/N]: ')).strip().lower()
    elif novamente == 'n':
        print('Encerrando o programa... obrigado.')
        break
