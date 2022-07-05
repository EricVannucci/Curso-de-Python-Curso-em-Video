print('\033[36mAnalisador de Triângulos.\033[m')
seg1 = int(input('Primeiro Seguimento: '))
seg2 = int(input('Segundo Seguimento: '))
seg3 = int(input('Terceiro Seguimento: '))
if seg2 < seg3 + seg1 and seg1 < seg3 + seg2 and seg1 < seg2 + seg3:
    print('É possível criar um triângulo com esses seguimentos, e ele será ', end='')
    if seg1 == seg2 == seg3:
        print('EQUILÁTERO.')
    elif seg1 != seg2 != seg3 != seg1:
        print('ESCALENO.')
    else:
        print('ISÓSCELES.')
else:
    print('Não é possível criar um triângulo com esses seguimentos!')
