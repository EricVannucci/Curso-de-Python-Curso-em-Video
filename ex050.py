soma = 0
cont = 0
print('\033[96mDigite seis números inteiros e pares:\033[m ')
for c in range(1, 7):
    num = int(input(f'Digite o {c}º número: '))
    if num % 2 == 0:
        soma = soma + num
        cont = cont + 1
print(f'Você informou {cont} número(s) PAR(ES) e a soma deles é {soma}')
