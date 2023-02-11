"""Exercício Python 076: Crie um programa que tenha uma tupla única com nomes de produtos e
seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando
os dados em forma tabular."""
soma = 0
produtos = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Transferidor',
            4.20, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)
print(51 * '=')
print(f"{'Lista de produto/preço:':^51}")
print(51 * '=')
for item in range(0, len(produtos), 2):
    print(f'{produtos[item]:.<40}', f'R$ {produtos[item+1]:>7.2f}')
    soma += produtos[item+1]
print(51 * '-')
print(f'A soma dos produtos é: R${soma:>7.2f}')
print(51 * '=')
