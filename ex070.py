linhas = '-'
titulo = 'Loja Super Baratão'
print(linhas * 60)
print(titulo.center(55))
print(linhas * 60)

soma = 0
mil = 0
barato = []
valor_menor = 900000000000000000000000

while True:
    produto = ' '
    while produto in ' ':
        produto = str(input('Nome do Produto: ')).strip().capitalize()
    valor = float(input('Valor R$: '))
    soma += valor
    if valor >= 1000:
        mil += 1
    if valor < valor_menor:
        valor_menor = valor
        barato = produto
    continua = ' '
    while continua not in 'sn':
        continua = str(input('Mais produtos? [S/N]: ')).strip().lower()[0]
    if continua == 'n':
        break
print('______________________FIM DO PROGRAMA______________________')
print(f'Total da sua compra foi R$ {soma:.2f}.')
if mil == 0:
    print('Não houve nenhum produto acima de mil Reais.')
else:
    print(f'Temos {mil} produto(s) acima de mil Reais.')
print(f'O produto mais barato foi {barato} que custou {valor_menor:.2f}')
