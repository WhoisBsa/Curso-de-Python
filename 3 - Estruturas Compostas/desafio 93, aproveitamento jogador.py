"""
Crie um programa que gerencie o aproveitamento de um jogador de futebol.
O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois
vai ler a quantidade de gols feitos em cada partida. No final, tudo isso
será guardado em um dicionário, incluindo o total de gols feitos durante
o campeonato.
"""


jogador = dict()
jogador['nome'] = str(input('Nome do jogador: '))
partidas = int(input('Quantidade de partidas: '))
gols = [] * partidas

for i in range(0, partidas):
    gols.append(int(input(f'Gols na {i+1}º partida: ')))

jogador['gols'] = gols
jogador['total'] = sum(gols)

print('=-=' * 15)
print(jogador)
print('=-=' * 15)

for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('=-=' * 15)

print(f'O jogador {jogador["nome"]} jogou {partidas} partidas.')
for i, v in enumerate(jogador['gols']):
    print(f'{"=>":>5}  Na partida {i+1}, fez {v} gols')
print(f'Foi um total de {jogador["total"]} gols.')
