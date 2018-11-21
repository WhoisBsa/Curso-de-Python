"""
Elabore um programa que calcule o valor a ser pago por um produto, considerando
o seu preço normal e condição de pagamento:
- À vista dinheiro/cheque: 10% de desconto
- À vista cartão: 5% de desconto
- Em até 2x no cartão: preço normal
- 3x ou mais: 20% de juros
"""

precoProd = float(input('Informe o preço do produto: R$'))
print("""Escolha uma forma de pagamento:
1 - À vista dinheiro/cheque: 10% de desconto
2 - À vista cartão: 5% de desconto
3 - Em até 2x no cartão: preço normal
4 - 3x ou mais: 20% de juros
""")
formPag = int(input('Forma de pagamento: '))

if formPag == 1:
    print('O valor do produto é: {}'.format(precoProd - precoProd * (10/100)))
elif formPag == 2:
    print('O valor do produto é: {}'.format(precoProd - precoProd * (5/100)))
elif formPag == 3:
    print('O valor do produto é: {}'.format(precoProd))
elif formPag == 4:
    print('O valor do produto é: R${}'.format(precoProd + precoProd * (20/100)))
else:
    print('Forma de pagamento inválida!')