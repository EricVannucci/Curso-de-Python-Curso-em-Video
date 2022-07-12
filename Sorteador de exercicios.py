from random import randint
from time import sleep
import pygame
pygame.init()
pygame.mixer.music.load('BossTheme MP3.mp3')
pygame.mixer.music.play()

print('\033[35m=\033[m'*37)
print('Sorteador de exercícios para revisão!')
print('\033[35m=\033[m'*37)
ex = int(input('\nDigite qual o último exercício estudado: '))
print('Sorteando...')
print('3')
sleep(1)
print('2')
sleep(1)
print('1')
sleep(1)
print('\033[35m=\033[m'*35)
print(f'O exercício para revisar hoje é {randint(1, ex)}')
print('\033[35m=\033[m'*35)
input()
