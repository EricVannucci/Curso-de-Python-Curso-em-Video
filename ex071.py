# cabeçalho

print('\033[96m=' * 30)
print('  * Bem-Vindo ao Banco CEV *')
print('=' * 30)
print('Cédulas disponíveis:\n50,00\n20,00\n10,00\n1,00')
saque = int(input('\033[mQUAL VALOR VOCÊ DESEJA SACAR?\nR$ '))
cinquenta = vinte = dez = um = total = 0

# contabilização de notas
while True:
    if saque != 0:
        total = saque - 50
        cinquenta += 1

    # resposta
    print(f'Total de {cinquenta} cédulas de R$50,00')
    print(f'Total de {vinte} cédulas de R$20,00')
    print(f'Total de {dez} cédulas de R$10,00')
    print(f'Total de {um} cédulas de R$1,00')

print(f'\033[96m* Obrigado por escolher o Banco CEV, tenha um bom dia! *')
