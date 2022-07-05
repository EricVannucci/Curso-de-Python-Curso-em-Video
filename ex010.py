print('Vamos converter o dinheiro que você tem na carteira por Dólar!')
r = float(input('Quantos Reais você tem na carteira? R$'))
d = 3.27
g = r/d
print('Você pode comprar {:.2f} Dólares com {:.2f} Reais'.format(g,r))

print('****Outra forma de fazer o exercício****')

print('Vamos converter os Reais que você tem na carteira por Dolar!')
r = float(input('Quantos Reais você tem? R$'))
d = float(input('Qual a cotação do Dolar hoje? '))
print(f'Você pode comprar {r/d:.2f} Dólares')