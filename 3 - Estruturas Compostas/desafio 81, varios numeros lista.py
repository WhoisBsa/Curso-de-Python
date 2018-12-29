"""
Crie um programa que vai ler vários números e colocar em um lista.
Depois disso, mostre:
A - Quantos números foram digitados;
B - A lista de valores ordenada de forma decrescente;
C - Se o valor 5 foi digitado e está ou não na lista.
"""

numeros = list()
cont = 0
while True:
    n = int(input('Digite um valor: '))
    cont += 1
    numeros.append(n)
    print('Valor adicionado com sucesso...')
    op = str(input('Quer continuar? [s/n]: '))
    if op not in 'SsNn':
        op = str(input('Apenas s (sim) ou n (não): '))
    if op in 'Nn':
        print('=-=' * 8)
        break
print(f'Foram digitados {cont} elementos')
numeros.sort(reverse=True)
print(f'Lista em ordem decrescente:{numeros}')
if 5 in numeros:
    print('O número 5 está presente na lista')
else:
    print('O número 5 não está presente na lista')
