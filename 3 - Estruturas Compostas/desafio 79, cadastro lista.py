"""
Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os
em uma lista. Caso o número já exista lá dentro, ele não será adicionado.
No final, serão exibidos todos os valores únicos difitados, em ordem
crescente.
"""

val = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in val:
        val.append(n)
        print('Valor adicionado com sucesso...')
        op = str(input('Quer continuar? [s/n]: '))
        if op not in 'SsNn':
            op = str(input('Apenas s (sim) ou n (não): '))
        if op in 'Nn':
            break
    else:
        print('Esse valor já existe')
print('-='*15)
val.sort()
print(f'Você digitou os valores {val}')
