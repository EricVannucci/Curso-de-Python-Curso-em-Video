from datetime import date
print('\033[34mDistribuidor de categoria CBA\033[m')
ano = int(input('Informe o ano de nascimento do atleta: '))
idade = date.today().year - ano
print(f'O atleta tem {idade} anos.')
if idade <= 9:
    print('O atleta é da categoria: \033[34mMIRIM\033[m.')
elif idade <= 14:
    print('O atleta é da categoria: \033[34mINFANTIL\033[m.')
elif idade <= 19:
    print('O atleta é da categoria: \033[34mJÚNIOR\033[m.')
elif idade <= 25:
    print('O atleta é da categoria: \033[34mSÊNIOR\033[m.')
else:
    print('O atleta é da categoria: \033[34mMASTER\033[m.')
