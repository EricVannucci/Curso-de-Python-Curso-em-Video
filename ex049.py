n = int(input('\033[31mDigite um número para saber sua tabuada: \033[m'))
for c in range(1, 11):
    print(f'{n} X {c:2} = {n*c}')
