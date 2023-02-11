"""Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou
se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo."""

from datetime import date
print(16*'\033[33m=-\033[m')
print('\033[32mALISTAMENTO MILITAR OBRIGATÓRIO\033[m')
print(16*'\033[33m-=\033[m')
ano = int(input('Ano de nascimento: '))
hoje = date.today().year
idade = hoje - ano
print(f'Quem nasceu em {ano} tem {idade} anos em {hoje}.')
if idade == 18:
    print('Você deve se alistar IMEDIATAMENTE!')
elif idade < 18:
    print(f'Ainda faltam {18 - idade} anos para seu alistamento, '
          f'que deverá ser em {ano + 18}')
else:
    print(f'Você já deve ter se alistado há {hoje - (ano + 18)} anos atrás, em {ano + 18}')
