from random import choice
from time import sleep
print(f'\033[34m{" Vamos Jogar? ":=^40}\033[m')
print('Escolha: \033[96mPEDRA\033[m, \033[35mPAPEL\033[m ou \033[34mTESOURA\033[m?')
opções = ['PEDRA', 'PAPEL', 'TESOURA']
jogador = str(input('Escreva sua escolha: ')).upper().strip()
computador = choice(opções)
print('\033[34mJô\033[m')
sleep(1)
print('\033[35mKen\033[m')
sleep(1)
print('\033[36mPô!!!\033[m')
print(29*'\033[7m=\033[m')
print(f'Você escolheu {jogador}')
print(f'O computador escolheu {computador}')
print(29*'\033[7m=\033[m')
if jogador == computador:
    print(f'\033[33mFoi um Empate!\033[m!')
elif jogador == 'PEDRA' and computador == 'PAPEL':
    print('\033[31mVocê Perdeu!\033[m')
elif jogador == 'PEDRA' and computador == 'TESOURA':
    print('\033[32mVocê Ganhou!\033[m')
elif jogador == 'PAPEL' and computador == 'PEDRA':
    print('\033[32mVocê Ganhou!\033[m')
elif jogador == 'PAPEL' and computador == 'TESOURA':
    print('\033[31mVocê Perdeu!\033[m')
elif jogador == 'TESOURA' and computador == 'PAPEL':
    print('\033[32mVocê Ganhou!\033[m')
elif jogador == 'TESOURA' and computador == 'PEDRA':
    print('\033[31mVocê Perdeu!\033[m')
else:
    print('\033[35mOpção INVALIDA!\033[m')
