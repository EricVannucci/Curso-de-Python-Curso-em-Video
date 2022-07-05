co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1 / 2)
print(f'A hipotenusa vai medir: {hi:.2f}')

print('****Outra forma de resolver o exercício:****')

import math
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
print(f'A hipotenusa vai medir {math.hypot(co, ca):.2f}')

print('****Outra forma de resolver o exercício importando apenas uma função****')

from math import hypot
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('comprimento do cateto adjacente: '))
print(f'A hipotenusa irá medit {hypot(co, ca):.2f}')
