"""Exercício Python 076: Crie um programa que tenha uma tupla única com nomes de produtos e
seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando
os dados em forma tabular."""

produtos = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Transferidor',
            4.20, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)
soma = 0
print(51*'=')
print(f"{'LISTA DE PRODUTOS/PREÇO':^50}")
print(51*'=')
print()

for item in range(0, len(produtos)):
    if item % 2 == 0:
        print(f'{produtos[item]:.<40}', end='')
    else:
        print(f'R${produtos[item]:>7.2f}')
        soma += produtos[item]
print(51*'=')
print(f'Valor total dos itens: R${soma:.2f}')
