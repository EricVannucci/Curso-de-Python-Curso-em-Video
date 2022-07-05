import math
angulo = float(input('Digite o ângulo desejado: '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print(f'O seno do ângulo informado é {seno:.2f}')
print(f'O cosseno do ângulo informado é {cosseno:.2f}')
print(f'A tangente do ângulo informado é {tangente:.2f}')

print('****Outra forma de resolver o exercício usando parte da biblioteca****')

from math import sin, cos, tan, radians
angulo = float(input('Digite o ângulo desejado: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print(f'O seno do ângulo informado é {seno:.2f}')
print(f'O cosseno do ângulo informado é {cosseno:.2f}')
print(f'A tangente do ângulo informado é {tangente:.2f}')
