sexo = str(input('Digite o seu sexo [M/F]: ')).strip().lower()
# while sexo not in 'mf': (também pode ser dessa forma!)
while sexo != 'f' and sexo != 'm':
    sexo = str(input('Dados inválidos digite "M" para masculino ou "F" para feminino: ')).strip().lower()
if sexo == 'm':
    sexo = 'Masculino'
elif sexo == 'f':
    sexo = 'Feminino'
print(f'Sexo {sexo} registrado!')
