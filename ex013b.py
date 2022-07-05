p = float(input('Digite o preço do produto:R$ '))
d = int(input('Digite o valor em porcentagem do desconto para pagamento a vista:% '))
a = int(input('Digite o valor em porcentagem de acréscimo para pagamento a prazo:% '))
print(f'O valor a vista é {p-(p*d/100):.2f} \nE a prazo é {p+(p*d/100):.2f}')