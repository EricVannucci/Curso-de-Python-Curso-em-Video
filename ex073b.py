classificacao = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro', 'Flamengo', 'Vasco',
                 'Chapecoense', 'Atlético MG', 'Botafogo', 'Athletico PR', 'Bahia', 'São Paulo',
                 'Fluminense', 'Sport', 'Vitória', 'Coritiba', 'Avaí', 'Ponte Preta', 'Atlético GO')

print(51 * '\033[32m-')
print('\033[34mClassificação Campeonato Brasileiro de Futebol 2017')
print(51 * '\033[33m-\033[m')
print('Escolha a informação desejada: ')
print('1. Cinco primeiros colocados\n'
      '2. Quatro últimos colocados\n'
      '3. Lista alfabética\n'
      '4. Colocação da Chapecoense\n'
      '5. Sair')
opcao = ' '
while True:
    opcao = (input('\nDigite o número da opção desejada: '))
    if opcao == '1':
        print(classificacao[:5])
    elif opcao == '2':
        print(classificacao[-4:])
    elif opcao == '3':
        print(sorted(classificacao))
    elif opcao == '4':
        chapecoense = classificacao.index('Chapecoense')
        print(f'A Chapecoense terminou o campeaonato na {chapecoense + 1}ª posição')
    elif opcao == '5':
        print('Saindo do programa, obrigado e até logo!')
        break
    else:
        print('Opção inválida, tente novamente: ')
