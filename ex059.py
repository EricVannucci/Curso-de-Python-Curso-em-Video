print(5 * '*', '\033[96mAnalisador de números\033[m', 5 * '*')

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

while True:
    menu = int(input('[1] somar\n'
                     '[2] multiplicar\n'
                     '[3] maior\n'
                     '[4] novos números\n'
                     '[5] sair do programa\n'))
    if menu == 1:
        print(f'\033[96mA soma entre {num1} e {num2} é {num1 + num2}.\033[m')
    elif menu == 2:
        print(f'\33[96mA multiplicação entre {num1} e {num2} é {num1 * num2}.\033[m')
    elif menu == 3:
        if num1 > num2:
            print(f'\033[96mO {num1} é maior que o {num2}.\033[m')
        elif num2 > num1:
            print(f'\033[96mO {num2} é maior que o {num1}.\033[m')
        elif num2 == num1:
            print('\033[96mOs dois números são iguais.\033[m')
    elif menu == 4:
        num1 = int(input('\033[96mDigite o primeiro número: \033[m'))
        num2 = int(input('\033[96mDigite o segundo número: \033[m'))
    elif menu == 5:
        print('\033[96mAté mais!\033[96m')
        exit()
    else:
        print('\033[96mOpção inválida, tente novamente...\033[m')
