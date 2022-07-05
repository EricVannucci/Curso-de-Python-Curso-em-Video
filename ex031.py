viagem = int(input('Digite a distancia que você quer viajar em quilometros: '))
print(f'Você está prestes a começar sua viagem de {viagem}km')
valor = viagem * 0.50 if viagem <= 200 else viagem * 0.45
print(f'Sua viagem vai custar: R${valor:.2f}')
print('Boa Viagem!')
