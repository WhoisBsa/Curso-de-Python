"""
Crie um programa onde 4 jogadores joguem um dado e tenham
resultados aleatórios. Guarde esses resultados em um ddicionário.
No final, coloque esse dicionário em ordem, sabendo que o vencedor
tirou o maior número no dado
"""

from random import randint
from time import sleep
from operator import itemgetter


jogadores = dict()
maior = 0
ranking = dict()

for i in range(0, 4):
    jogadores[f'jogador{i+1}'] = randint(1, 6)

print('Valores Sorteados: ')
for k, v in jogadores.items():
    print(f'{k}: {v}')
    sleep(1)

ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
print('Ranking dos jogadores:')
for k, v in enumerate(ranking):
    print(f'{k+1}º lugar {v[0]}: {v[1]}')
    sleep(1)
