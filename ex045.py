from random import randint
from time import sleep
import pygame

pygame.init()
pygame.mixer.music.load('jokenpo.mp3')
# Intro Game
print(f'\033[34m{" Vamos Jogar? ":=^40}\033[m')
print(f'{"Suas Opções:":^40}')
pygame.mixer.music.play()

# Menu Game
print('\033[34m [1] PEDRA\n [2] PAPEL\n [3] TESOURA\033[m')
jogador = int(input('Qual a sua jogada? '))

# Opção Jogador
if jogador > 3:
    print('\033[31mSeu trapaceiro, não existe essa opção!!\033[m')
else:
    computador = randint(1, 3)
    print('\033[96mJO\033[m')
    sleep(2)
    print('\033[36mKEN\033[m')
    sleep(2)
    print('\033[91mPO!!!\033[m\n')
    sleep(2)
    print(14 * '=-')

# Opções do jogador
    if jogador == 1:
        print('O jogador escolheu PEDRA')
    elif jogador == 2:
        print('O jogador escolheu PAPEL')
    elif jogador == 3:
        print('O jogador escolheu TESOURA')

# Opções do computador
    if computador == 1:
        print('O computador escolheu PEDRA')
    elif computador == 2:
        print('O computador escolheu PAPEL')
    elif computador == 3:
        print('O computador escolheu TESOURA')
    print(14 * '-=')

# Resultado da partida
if jogador == 1 and computador == 1:
    print('\033[1;97;43mEMPATE!!\033[m')
elif jogador == 1 and computador == 2:
    print('\033[1;97;41mVOCÊ PERDEU!!\033[m')
elif jogador == 1 and computador == 3:
    print('\033[1;97;42mVocê GANHOU!!\033[m')
elif jogador == 2 and computador == 2:
    print('\033[1;97;43mEMPATE!!\033[m')
elif jogador == 2 and computador == 3:
    print('\033[1;97;41mVOCÊ PERDEU!!\033[m')
elif jogador == 2 and computador == 1:
    print('\033[1;97;42mVocê GANHOU!!\033[m')
elif jogador == 3 and computador == 3:
    print('\033[1;97;43mEMPATE!!\033[m')
elif jogador == 3 and computador == 1:
    print('\033[1;97;41mVOCÊ PERDEU!!\033[m')
elif jogador == 3 and computador == 2:
    print('\033[1;97;42mVocê GANHOU!!\033[m')
input()
