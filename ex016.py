import math
n = float(input('Digite um número: '))
i = int(n)
print('O número {} tem a parte inteira {}'.format(n,i))

n = float(input('Digite um número: '))
print('O número digitado {} tem a parte inteira {}.'.format(n, math.trunc(n)))

n = float(input('Digite um número: '))
print('O número {} tem a parte inteira {}.'.format(n, int(n)))
