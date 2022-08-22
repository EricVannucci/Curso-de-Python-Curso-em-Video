while True:
    num = int(input('\033[96m Quer ver a tabuada de qual número? \033[m'))
    print(36 * '\033[34m~\033[m')
    if num < 0:
        print('\033[91mPrograma de tabuada encerrado, volte sempre!\033[m')
        break
    else:
        print(f'{num} X 1  = {num * 1}')
        print(f'{num} X 2  = {num * 2}')
        print(f'{num} X 3  = {num * 3}')
        print(f'{num} X 4  = {num * 4}')
        print(f'{num} X 5  = {num * 5}')
        print(f'{num} X 6  = {num * 6}')
        print(f'{num} X 7  = {num * 7}')
        print(f'{num} X 8  = {num * 8}')
        print(f'{num} X 9  = {num * 9}')
        print(f'{num} X 10 = {num * 10}')
        print(36 * '\033[34m~\033[m')
