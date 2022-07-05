import random
num = (int(input('Vou pensar em um número de 1 a 10, tente adivinhar digitando aqui: ')))
escolha = random.randint(1, 10)
print(f'Vejaaaaamos... eu pensei em {escolha}')
if num == escolha:
    print('Você acertou!')
else:
    print('Você errou!')
