print('\033[35mCalculadora de IMC (índice de massa corpórea)\033[m')
peso = float(input('Digite seu peso (kg): '))
altura = float(input('Digite sua altura (m): '))
imc = peso / (altura * altura)
print(f'O seu IMC é {imc:.1f}')
if imc < 18.4:
    print('Você está \033[35mABAIXO DO PESO\033[m')
elif 18.5 < imc < 24.9:
    print('Você está com \033[35mPESO IDEAL\033[m')
elif 25 < imc < 29.9:
    print('Você está com \033[35mSOBREPESO\033[m')
elif 30 < imc < 39.9:
    print('Você está com \033[35mOBESIDADE\033[m')
else:
    print('Você está com \033[35mOBESIDADE MÓRBIDA\033[m, \033[31mCUIDADO!\033[m')
