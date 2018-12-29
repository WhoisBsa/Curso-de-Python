"""
Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os valores
pares e os valores impares digitados, repectivamente.
Ao final, mostre o conteúdo das três listas geradas.
"""

numeros = list()
par = list()
impar = list()
while True:
    n = int(input('Digite um valor: '))
    numeros.append(n)
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
    print('Valor adicionado com sucesso...')
    op = str(input('Quer continuar? [s/n]: '))
    if op not in 'SsNn':
        op = str(input('Apenas s (sim) ou n (não): '))
    if op in 'Nn':
        print('=-=' * 8)
        break
print(f'Lista: {numeros}')
print(f'Pares: {par}')
print(f'Ímpar: {impar}')
