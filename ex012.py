print('====Informe o valor atual do item para saber o valor com desconto de 5%====')
v = float(input('Valor: '))
d = 5
r = v-(v*0.05)
print('O valor com desconto é {:.2f}'.format(r))
print('****Outra forma de fazer o exercício****')
print('==== informe o valor atual e valor do desconto ====')
v = float(input('Valor: R$'))
d = float(input('Valor do desconto: %'))
r = v-(v * d/100)
print(f'O valor com desconto de {d:.0f}% do produto é {r:.2f}')
