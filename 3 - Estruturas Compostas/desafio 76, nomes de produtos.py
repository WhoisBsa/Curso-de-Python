"""
Crie um programa que tenha uma tupla única com nomes de produtos
e seus respectivos preços, na sequência.
No final, mostre uma listagem de preços, organizando
os dados em forma tabular.
"""

listagem = ('Lápis', 1, 'Borracha', 2, 'Caderno', 15.90,
            'Estogo', 10, 'Transferidor', 4.20, 'Compasso', 9.99,
            'Mochila', 120, 'Canetas', 22.50, 'Livro', 34.90)

print('-'*39)
print(f'{"LISTAGEM DE PREÇOS":^39}')
print('-'*39)

for i in range(0, len(listagem)):
    if i % 2 == 0:
        print(f'{listagem[i]:.<30}R$', end='')
    else:
        print(f'{listagem[i]:>7.2f}')

print('-'*39)
