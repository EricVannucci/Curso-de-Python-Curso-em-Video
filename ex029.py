velocidade = int(input('Digite a velocidade do veículo em KM/h: '))
multa = (velocidade - 80)*7
if velocidade <= 80:
    print('Velocidade permitida na via.')
else:
    print('Velocidade incompatível com a permitida na via.')
    print(f'Multa devida: R${multa:.2f}')
