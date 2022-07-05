print(f'\033[34m{" Lojas Vannucci ":=^40}\033[m')
preço = float(input('Digite o valor das compras: R$ '))
print(f'\33[34m{"FORMAS DE PAGAMENTO:":^40}\033[m')
print('\n'
      '[1] A vista dinheiro/pix\n'
      '[2] A vista cartão de débito\n'
      '[3] 2X no cartão de crédito\n'
      '[4] 3X ou mais no cartão de crédito\n')
forma = int(input('Digite sua opção de pagamento: '))
if forma == 1:
    print(f'Para pagamento a vista suas compras tem 10% de desconto e saem '
          f'por R$ {preço - (preço * 10 / 100):.2f}')
elif forma == 2:
    print(f'Para pagamento a vista no débito suas compras tem 5% de desconto e '
          f'saem por R$ {preço - (preço * 5 / 100):.2f}')
elif forma == 3:
    print(f'Para pagamento em 2X no cartão suas compras saem por R$ {preço:.2f}, '
          f'em duas parcelas de R$ {preço / 2:.2f}')
elif forma == 4:
    vezes = int(input('Quantas vezes você quer dividir? '))
    if vezes < 3:
        print('\033[31mQuantidade invalida de parcelas, devem ser acima de 3 vezes!\033[m')
    else:
        print(f"Para pagamento em {vezes}X suas compras tem 20% de juros e "
              f"saem por {preço + (preço * 20 / 100):.2f} com "
              f"parcelas de R$ {(preço + (preço * 20 / 100)) / vezes:.2f}")
else:
    print('\033[31mOpção inválida, tente novamente!\033[m')
print('\033[34mObrigado por comprar conosco, atendemos bem para atender sempre! volte logo!\033[m')
