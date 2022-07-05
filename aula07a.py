n1 = int(input('Digite um número: '))
n2 = int(input('Digite um outro número: '))
s = n1 + n2
su = n1 - n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {},\n a subtração é {},\n a multiplicação é {},\n a divisão é {:.2f},\n a divisão inteira é {},\n a exponenciação é {}'.format(s,su,m,d,di,e))
print('A soma é {}'.format(s), end='; ')
print('A subtração é {}'.format(su))
print('A multiplicação é {:.3}'.format(d), end='; ')
print('A divisão é {}'.format(d))
print('A divisão inteira é {}'.format(di))
print('A exponenciação é {}'.format(e))