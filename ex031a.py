viagem = int(input('Qual a distância da sua viagem em quilometros? '))
print(f'Você está prestes a começar sua viagem de {viagem}km')
if viagem > 200:
    print(f'Sua viagem vai custar no valor promocional: R${viagem*0.45:.2f}')
else:
    print(f'Sua viagem vai custar: R${viagem*0.50:.2f}')
print('Boa Viagem!')
