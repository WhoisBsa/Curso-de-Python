"""
Desenvolva um programa que leia o primeiro termo e a razao de um PA.
No final, mostre aos 10 primeiros termos dessa progressão
"""

print('-'*5, 'Gerador de PA', '-'*5)
p = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razao da sua PA: '))
d = p + (10 - 1) * r
for i in range(p, d + r, r):
    print('{}'.format(i), end=' - ')
print('Acabou')
