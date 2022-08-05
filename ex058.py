from random import randint
from time import sleep
import pygame

# carregando música
pygame.init()
pygame.mixer.music.load('Concentration.mp3')
pygame.mixer.music.play()

# contadores
tentativas = 0
pontos = 0

# título e pergunta
print('\033[96m+-----ADIVINHAÇÃO------+\033[m')
jogo = str(input('\033[94mOla, sou seu computador!\nVamos jogar?\033[m'
                 ' [\033[92mS\033[m/\033[91mN\033[m]: ')).strip().lower()
if jogo == 's':
    print('Oba!!! vamos lá...')
elif jogo == 'n':
    print('\033[31mQue pena... Então tá, TCHAU!\033[m')
    exit()
print('Vou pensar em um número entre 0 e 10')
print('Hummmmm.... ')
sleep(1)
computador = randint(0, 10)
# print(computador)
num = int(input('Já sei!! Qual o seu palpite? '))
tentativas = 1

# processamento
while computador != num:
    if num > 10:
        print(f'{num} é maior que 10!')
        num = int(input('Escolha entre 0 e 10: '))
        tentativas += 1
    elif computador > num:
        print('Foi pouco, mais...')
        num = int(input('Tente novamente: '))
        tentativas += 1
    elif computador < num:
        print('Foi muito, menos...')
        num = int(input('Tente novamente: '))
        tentativas += 1

# resposta e pontuação
pontos = 11 - tentativas
if computador == num:
    print(f'Você acertou com {tentativas} tentativas!! Também escolhi {computador}')
    print(f'Você fez {pontos} pontos!')
if pontos == 10:
    print('\033[32mUAU! Você por acaso é vidente??')
elif pontos > 8:
    print('\033[34mVocê é bom nisso!!')
elif 7 > pontos > 5:
    print('\033[33mMeh... ok...')
elif 4 > pontos > 1:
    print('\033[36mTá ruim, hein!')
elif pontos <= 0:
    print('\033[95mApelão! kkkkkk')
input()
