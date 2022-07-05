tempo = (int(input('Quantos anos tem o seu carro? ')))
if tempo <= 3:
    print('Carro Novo!')
else:
    print('Carro Véio!')

nome = str(input('Qual o seu carro? '))
if nome == 'Fusca':
    print('Que carro irado você tem!!!')
else:
    print('Seu carro é tão sem graça...')
print(f'Parabéns pelo seu {nome}.')
print()
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print(f'Sua média foi {m:.1f}')
print('PARABÉNS' if m >=6.0 else'Você precisa estudar mais!')
