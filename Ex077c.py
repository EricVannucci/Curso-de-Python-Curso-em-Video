"""Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais."""

contador = 0
lista_palavras = []

print('\033[96mDigite cinco palavras para saber quais as vogais em cada.\033[m\n')
while contador != 5:
    palavras = input('Digite uma palavra: ').strip().upper()
    contador += 1
    lista_palavras.append(palavras)
print(f'A lista de palavras digitadas é: {lista_palavras}')
for palavras in lista_palavras:
    print(f'\nA palavra {palavras} as vogais são: ', end=' ')
    for letra in palavras:
        if letra in 'AEIOU':
            print(letra, end=' ')

"""execercicio feito sem uma tupla, sim uma lista para que o usuário digite suas palavras"""
