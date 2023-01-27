from random import randint

sorteio = (randint(1, 50), randint(1, 50), randint(1, 50), randint(1, 50), randint(1, 50))
print('Os números sorteados foram: ', end='')
for n in sorteio:
    print(f'{n} ', end='')
print(f'\nO maior número sorteado foi {max(sorteio)}')
print(f'O menor número sorteado foi {min(sorteio)}')
