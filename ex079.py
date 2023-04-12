produtos = ["iPhone", "iPad", "Airpod", "MacBook"]
precos = [7000, 1000, 2500, 14000]
precos_imposto = []

for preco in precos:
    imposto = (preco * 1.1)
    precos_imposto.append(imposto)


for i in range (len(precos_imposto)):
    produto = produtos[i]
    preco_imposto = precos_imposto[i]
    print(f"{produto}, {preco_imposto:.2f}")
