from random import randint

sorteio = (randint(1, 50), randint(1, 50), randint(1, 50), randint(1, 50), randint(1, 50))
print('Os númeoros sorteados são:')
print(sorteio)
print(f'O maior número sorteado foi: {max(sorteio)}')
print(f'O menor número sorteado foi: {min(sorteio)}')
