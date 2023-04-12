""" Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
"""

lista = lista_min = lista_max = []

for p in range(0, 5):
    lista.append(int(input(f'Digite o {p}º valor: ')))

print(16 * '*-*')
print(f"Você digitou os seguintes valores {lista}")
print(16 * '*-*')

for posicao, lista in enumerate(lista):
    if posicao == max(lista):
        lista_max.append(posicao)

print(f"O maior valor digitado foi {max(lista)} e sua posição foi {lista_max}")
print(f"O menor valor digitado foi {min(lista)} e sua posição foi {lista_min}")
