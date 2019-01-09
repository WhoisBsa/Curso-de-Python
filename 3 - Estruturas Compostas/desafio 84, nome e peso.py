"""
Faça um programa que leia nome e peso de várias pessoas, guardando
tudo em uma lista. No final, mostre:
A - Quantas pessoas foram cadastradas.
B - Uma listagem com as pessoas mais pesadas.
C - Uma listagem com as pessoas mais leves.
"""

#   Declaração de variáveis
pessoas = list()
dados = list()
maiorpeso = menorpeso = 0

#   Cadastro de pessoas
while True:
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Peso: ')))

    #   Se a lista for vazia o maior e o
    #   menor peso serão iguais
    if len(pessoas) == 0:
        maiorpeso = menorpeso = dados[1]
    else:
        if dados[1] > maiorpeso:
            maiorpeso = dados[1]
        if dados[1] < menorpeso:
            menorpeso = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    op = str(input('Quer continuar? [s/n]: '))
    if op not in 'SsNn':
        op = str(input('Apenas s (sim) ou n (não): '))
    if op in 'Nn':
        print('=-=' * 8)
        break

print(f'Foram cadastradas {len(pessoas)} pessoas.')
print(f'Quem teve o maior peso foi de {maiorpeso}kg,', end=' ')
for p in pessoas:
    if p[1] == maiorpeso:
        print(f'{p[0]}')

print(f'Quem teve o menor peso foi de {menorpeso}kg,', end=' ')
for p in pessoas:
    if p[1] == menorpeso:
        print(f'{p[0]}')
