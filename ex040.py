print('\033[35mCalculadora de médias\033[m')
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
print(f'Considerando as notas {nota1} e {nota2} a média do aluno é {media}')
if media < 5:
    print('O aluno está \033[31mREPROVADO\033[m.')
elif 6 <= media < 9.9:
    print('O aluno está \033[32mAPROVADO\033[m.')
elif media == 10:
    print('Parabéns pela média perfeita! o aluno esta \033[32mAPROVADO\033[m.')
else:
    print('O aluno está de \033[33mRECUPERAÇÃO\033[m.')
