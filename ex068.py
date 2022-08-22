from random import randint

print('=-' * 13)
print('\033[96mVamos jogar par ou ímpar?\033[m')
print('-=' * 13)

contador = 0

while True:
    valor = int(input('Diga um valor: '))
    jogada = ' '
    while jogada not in 'pi':
        jogada = str(input('Par ou Ímpar? [P/I]: ')).strip().lower()
    computador = randint(1, 13)
    if (computador + valor) % 2 == 0:
        print(f'Você jogou {valor} e eu joguei {computador}. Total de {valor + computador} que é Par')
        if jogada == 'p':
            print('Você ganhou!')
            contador += 1
        else:
            print('Você perdeu!')
            break
    else:
        print(f'Você jogou {valor} e eu joguei {computador}. Total de {valor + computador} que é Ímpar')
        if jogada == 'i':
            print('Você ganhou!')
            contador += 1
        else:
            print('Você perdeu!')
            break
print('=-' * 17)
print(f'Game Over!!! Você ganhou {contador} vezes.')
print('-=' * 17)
