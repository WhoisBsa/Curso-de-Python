"""
Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar.
No final, mostre:
A - Qual é o total gasto na compra
B - Quantos produtos custam mais de R$1000
C - Qual é o nome do produto mais barato
"""

print("""
=-=-=-=-=-=-=-=-=
=   Loja Loca   =
=-=-=-=-=-=-=-=-=
""")

total = 0
maisquemil = 0
cont = 0
nmaisbarato = ''
precomaisbarato = 0

while True:
    produto = str(input('Nome do Produto: ')).strip()
    preco = float(input('Preço: R$'))
    cont += 1

    # Soma o preço total de produtos
    total += preco

    # Conta quantos produtos maiores que R$1000
    if preco >= 1000:
        maisquemil += 1

    # Verifica qual o produto mais barato
    if cont == 1:
        precomaisbarato = preco
        nmaisbarato = produto
    else:
        if preco < precomaisbarato:
            precomaisbarato = preco
            nmaisbarato = produto

    # Pergunta ao usuário se ele quer continuar, enquanto não for
    # S ou N o programa não para de perguntar
    print('-' * 24)
    op = ' '
    while op not in 'SsNn':
        op = str(input('Quer continuar? [S/N] ')).strip().upper()
    if op in 'Nn':
        break

print('=-=' * 8)
print('FIM DA COMPRA')
print('=-=' * 8)
print(f'O total da compra foi de R${total:.2f}')
print(f'Temos {maisquemil} produtos custando mais que R$1000.00')
print(f'O produto mais barato foi {nmaisbarato} que custa R${precomaisbarato:.2f}')