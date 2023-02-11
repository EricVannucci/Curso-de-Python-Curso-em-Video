"""Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras
(não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais."""

palavras = ('Clara', 'Cibelle', 'Bernardo', 'Snoopy', 'Catarina', 'Volkswagen', 'Fusca', 'Karl')

for item in palavras:
    vogais = ''
    for c in range(0, len(item)):
        vogal = item[c]
        if vogal == 'a' or vogal == 'e' or vogal == 'i' or vogal == 'o' or vogal == 'u':
            vogais += vogal + ' '
    print(f'Na palavra {item} temos as vogais: {vogais}')
