print('\033[96m****Analisador de números****\033[m')
n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
while True:
    print('[1] Somar\n'
          '[2] Multiplicar\n'
          '[3] Maior\n'
          '[4] Novos números\n'
          '[5] Sair\n')
    opcao = int(input('Digite sua opção: '))
    print()
    if opcao == 1:
        print(f'A soma entre {n1} e {n2} é {n1 + n2}.\n')
    elif opcao == 2:
        print(f'A multiplicação entre {n1} e {n2} é {n1 * n2}.\n')
    elif opcao == 3:
        if n1 > n2:
            print(f'{n1} é maior que {n2}.\n')
        elif n2 > n1:
            print(f'{n2} é maior que {n1}.\n')
        else:
            print('Os dois números são iguais!\n')
    elif opcao == 4:
        print('Escolha novos números:')
        n1 = int(input('Digite um número: '))
        n2 = int(input('Digite outro número: '))
        print()
    elif opcao == 5:
        print('Até mais!!')
        exit()
    else:
        print('Opção inválida, tente novamente...\n')
