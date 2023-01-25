print('\033[33mESCOLA CARLITOS')
print(15*'-')
print('\033[m')

# input das informações e cálculo da média
nome = str(input('Favor inserir nome do aluno: ')).title().strip()
nota1 = float(input('Informe a nota do primeiro semestre: '))
nota2 = float(input('Informe a nota do segundo semestre: '))
nota3 = float(input('Informe a nota do terceiro semestre: '))
nota4 = float(input('Informe a nota do quarto semestre: '))
media = (nota1 + nota2 + nota3 + nota4) / 4

# Verificação da aprovação e aproveitamento do aluno
if media >= 9:
    print(f'O aluno(a) {nome} obteve média {media:.1f} e está \033[32mAPROVADO!\033[m')
    print('O aproveitamento foi: A')
    print('PARABÉNS!')
elif media >= 8:
    print(f'O aluno(a) {nome} obteve média {media:.1f} e está \033[32mAPROVADO!\033[m')
    print('O aprovietamento foi: B')
elif media >= 6:
    print(f'O aluno(a) {nome} obteve média {media:.1f} e está \033[32mAPROVADO!\033[m')
    print('O aproveitamento foi: C')
elif media >= 4:
    print(f'O aluno(a) {nome} obteve média {media:.1f} e está \033[31mREPROVADO\033[m')
    print('O aproveitamento foi: D')
else:
    print(f'O aluno(a) {nome} obteve média {media:.1f} e está \033[31mREPROVADO\033[m')
    print('O aproveitamento foi: E')
