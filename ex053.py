frase = str(input('Digite uma frase: ')).upper().strip().replace(' ', '')
print(f'O inverso da frase {frase} é {frase [::-1]}')
if frase == frase[::-1]:
    print('Essa frase é um palíndromo')
else:
    print('Essa frase não é um palíndromo')
