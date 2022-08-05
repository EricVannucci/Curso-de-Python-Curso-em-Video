# variáveis
media = 0
homem = 0
velho = 0
nome_velho = ''
mulher = 0

# questionário
for c in range(1, 5):
    print(f'----{c}ª Pessoa----')
    nome = str(input('Nome: ')).strip().title()
    idade = int(input('Idade: '))
    sexo = str(input('[M/F]: ')).strip().upper()

# sistema
    media += idade
    if sexo == 'F' and idade < 20:
        mulher += 1
    if sexo == 'M':
        homem += 1
        if idade > velho:
            velho = idade
            nome_velho = nome

# dados finais
print(f'A média de idade do grupo é {media/4:.0f} anos.')
if mulher == 0:
    pass
else:
    print(f'No grupo existe(m) {mulher} mulher(es) abaixo de 20 anos.')
if homem == 0:
    pass
else:
    print(f'O homem mais velho é {nome_velho} e ele tem {velho} anos.')
