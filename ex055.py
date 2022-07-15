lista = []
for c in range(1, 6):
    peso = float(input(f'Peso da {c}ª pessoa: '))
    lista += [peso]
print(f'O maior peso lido é: {max(lista)}Kg')
print(f'O menor peso lido é: {min(lista)}Kg')
