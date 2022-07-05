a = int(input('Digite um número: '))
b = int(input('Digite mais um número: '))
c = int(input('Digite outro número: '))
menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
print(f'O menor número escolhido foi {menor}')
maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
print(f'O maior número escolhido foi {maior}')
