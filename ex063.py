print('~' * 21)
print(' Sequência Fibonacci')
print('~' * 21)
t1 = 0
t2 = 1
termos = int(input('Quantos termos você quer ver da sequência de Fibonacci? '))
print(f'{t1} → {t2} → ', end='')
t3 = t1 + t2
cont = 3
while cont <= termos:
    t3 = t1 + t2
    print(f'{t3} → ', end='')
    t1 = t2
    t2 = t3
    cont += 1
print('FIM')
