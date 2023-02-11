"""Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais."""

lista_palavras = ('Clara', 'Bella', 'Sergio', 'Sandra', 'Bernardo', 'Marta', 'Rosa',
                  'Maylla', 'Maira', 'Snoopy', 'Catarina', 'Karl')

for palavra in lista_palavras:
    print(f'\nA palavra {palavra.upper()} possui as seguintes vogais: ', end='')
    for letra in palavra:
        if letra.upper() in 'AEIOU':
            print(letra.upper(), end=' ')
