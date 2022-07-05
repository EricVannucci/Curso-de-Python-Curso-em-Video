num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
num3 = int(input('Digite mais um número: '))
print(f'Você escolheu {num1}, {num2} e {num3}, correto?')
lista = [num1, num2, num3]
print(f'O menor número digitado foi {min(lista)}')
print(f'O maior número digitado foi {max(lista)}')
