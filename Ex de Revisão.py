"""Exercício Python 073: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do
Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da Chapecoense."""

classificacao = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro', 'Flamengo', 'Vasco',
                 'Chapecoense', 'Atlético MG', 'Botafogo', 'Athletico PR', 'Bahia', 'São Paulo',
                 'Fluminense', 'Sport', 'Vitória', 'Coritiba', 'Avaí', 'Ponte Preta', 'Atlético GO')
print(50 * '=-')

print(f'Os cinco primeiros colocados do campeonato de 2017 são: \n{classificacao[:5]}')

print(50 * '=-')

print(f'Os quatro últimos colocados do campeonato de 2017 são: \n{classificacao[-4:]}')

print(50 * '=-')

print(f'Os times em ordem alfabética: \n{sorted(classificacao)}')

print(50 * '=-')

print()

