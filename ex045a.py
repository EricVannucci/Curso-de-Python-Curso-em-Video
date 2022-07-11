from random import randint
from time import sleep

# Cabeçalho do jogo
print('=-=' * 11)
print('====\033[31m Vamos Jogar Jo Kem Pô?\033[m =====')
print('=-=' * 11)

# Opções e Menu
opções = ('Pedra', 'Papel', 'Tesoura')
print(f'''\033[31m{"Suas opções:":^30}\033[m\n
[0] Pedra
[1] Papel
[2] Tesoura''')
jogador = int(input('Digite sua opção: '))
computador = randint(0, 2)
if jogador > 2:
    print('\033[91mtesc, tesc... opção inválida...\033[m')
else:
    print('\033[94mJo\033[m')
    sleep(1)
    print('\033[34mKen\033[m')
    sleep(1)
    print('\033[35mPô!!!\033[m')

    # Verificação das jogadas
    print('=-=' * 9)
    print(f'Você jogou {opções[jogador]}')
    print(f'O computador jogou {opções[computador]}')
    print('=-=' * 9)
    if computador == 0:
        if jogador == 0:
            print('\033[33mEMPATE!\033[m')
        elif jogador == 1:
            print('\033[32mVocê GANHOU!\033[m')
        elif jogador == 2:
            print('\033[31mVocê PERDEU!\033[m')
    if computador == 1:
        if jogador == 0:
            print('\033[31mVocê PERDEU!\033[m')
        elif jogador == 1:
            print('\033[33mEMPATE!\033[m')
        elif jogador == 2:
            print('\033[32mVocê GANHOU!\033[m')
    if computador == 2:
        if jogador == 0:
            print('\033[32mVocê GANHOU!\033[m')
        elif jogador == 1:
            print('\033[31mVocê PERDEU!\033[m')
        elif jogador == 2:
            print('\033[33mEMPATE!\033[m')
