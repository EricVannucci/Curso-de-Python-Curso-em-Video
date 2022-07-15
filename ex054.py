from datetime import date
maior = 0
menor = 0
atual = date.today().year
for c in range(1, 8):
    ano = int(input(f'Digite o ano de nascimento da {c}ª pessoa: '))
    if atual - ano >= 21:
        maior += 1
    elif atual - ano < 21:
        menor += 1
print(f'{maior} pessoas são maiores de idade')
print(f'{menor} pessoas são menores de idade')
