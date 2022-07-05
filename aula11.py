nome = str(input('Qual é o seu nome? ')).title()
if nome == 'Eric':
    print('Que nome incrível!')
elif nome == 'José' or nome == 'Maria' or nome == 'João':
    print('Seu nome é bem comum...')
elif nome in 'Clara Bernardo Cibelle Sandra Marta':
    print('Lindo o seu nome!')
elif nome in 'Maíra Maylla':
    print('Diferentão seu nome, né?')
else:
    print('Que nome sem graça...')
print(f'Tenha um bom dia, {nome}!')
