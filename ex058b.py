# importações

from random import randint
from time import sleep
import pygame

# carregando música

pygame.init()
pygame.mixer.music.load('Concentration.mp3')
pygame.mixer.music.play()

# contadores
acertou = False
palpites = 0

# enunciado
print('Olá, sou seu computador.')
print('Vou pensar em um número entre 0 e 10, consegue acertar?')

# interação jogador
jogo = str(input('Você quer jogar comigo? [S/N]: ')).lower().strip()
if jogo == 'n':
    print('Então tá, tchau!')
    exit()
elif jogo == 's':
    print('Legal!! vou pensar em um número... vejamos...')
    computador = randint(0, 10)
sleep(1)
print('Pensei!')
print(computador)

# resultados
while not acertou:
    jogador = int(input('Qual o seu palpite? '))
    palpites += 1
    if jogador > 10:
        print(f'{jogador} não vale, tente novamente um número entre 0 e 10!')
    elif jogador > computador:
        print('Foi muito, tente novamente')
    elif jogador < computador:
        print('Foi pouco, tente novamente')
    elif computador == jogador:
        acertou = True
        print(f'Você acertou em {palpites} palpite(s)!')
if palpites == 1:
    print('Uau, você é vidente??')
elif palpites >= 10:
    print('Chutou bastante, hein!?')
else:
    print('Parabéns!')
input()
