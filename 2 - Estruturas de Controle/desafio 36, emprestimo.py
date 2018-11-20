"""
Escreva um programa para aprovar o empréstimo bancário para a compra de uma
casa. O programa vai perguntar o valor da casa, o salário do comprador e em
quantos anos ele vai pagar.

Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do
salário ou então o empréstimo será negado
"""

casa = int(input('Qual o valor da casa? '))
salario = float(input('Salário: '))
anos = int(input('Anos: '))
prestacao = float((casa/(12*anos)))

print('Valor da prestação: R${:.2f}'.format(prestacao))

if salario*0.30 >= prestacao:
    print('O banco aprova o seu empréstimo')
else:
    print('O banco não aprova o seu empréstimo')

