"""
Refaça o desafio 51 utilizando while
"""

print('-'*5, 'Gerador de PA', '-'*5)
p = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razao da sua PA: '))
termo = p
cont = 1
while cont <= 10:
    print('{}'.format(termo), end=' - ')
    termo += r
    cont += 1
print('Acabou')
