velocidade = int(input('Digite a velocidade em KM/h: '))
if velocidade > 80:
    print('Você excedeu a velocidade máxima da via, 80KM/h')
    multa = (velocidade - 80) * 7
    print(f'Sua multa por excesso de velocidade é de R${multa:.2f}')
print('Dirija com segurança, tenha um bom dia!')
