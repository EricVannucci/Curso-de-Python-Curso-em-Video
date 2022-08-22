while True:
    num = int(input('Quer ver a tabuada de qual número? '))
    print(17 * '\033[96m-=\033[m')
    if num < 0:
        print('\033[91mPrograma de tabuada encerrado, volte sempre!\033[m')
        break
    else:
        for c in range(1, 11):
            print(f'{num} X {c} = {num * c}')
        print(17 * '\033[96m-=\033[m')
