# variáveis
media = 0
nome_velho = []
idade_velho = 0
mulher_nova = 0
homem = 0
# questionário
for c in range(1, 5):
    print(f'----{c}ª Pessoa----')
    nome = str(input('Nome: ')).strip().title()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).lower()

# validações
    media += idade
    if sexo == 'm':
        if idade > idade_velho:
            idade_velho = idade
            nome_velho = nome
            homem += 1
    if sexo == 'f':
        if idade <= 20:
            mulher_nova += 1

# respostas
print(f'A idade média do grupo é {media / 4:.0f} anos.')
if homem == 0:
    print('Não existem homens no grupo.')
else:
    print(f'O homem mais velho tem {idade_velho} anos e se chama {nome_velho}.')
if mulher_nova == 0:
    print('Não existem mulheres com menos de 20 anos no grupo.')
else:
    print(f'Existe(m) {mulher_nova} mulher(e)s abaixo de 20 anos.')
