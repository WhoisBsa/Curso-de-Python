"""
Crie uma tupla preenchida com os 20 primeiros colocados da Tabela
do CBF, na ordem de colocação. Depois mostre:
A - Apenas os 5 primeiros colocados;
B - Os últimos 4 colocados da tabela;
C - Uma lista com os times em ordem alfabética;
D - Em que posição na tabela está o tima do Galo.
"""

times = ('Cruzeiro Esporte Clube',
         'Clube de Regatas Flamengo',
         'Clube Atlético Mineiro',
         'Chapecoense Esporte Clube',
         'Fluminense Esporte Clube',
         'Bahia Futebol Clube',
         'Vasco da Gama',
         '15 de Piracicaba',
         'Certaozinho Futebol Clube',
         'Atlético Paranaense',
         'Goias Esporte Clube',
         'Sao Paulo FC',
         'Corintinhas FC',
         'Palmeiras FC',
         'Criciúma FC',
         'Gremio Esporte Clube',
         'Sport',
         'Bota Fogo',
         'América Mineiro',
         'Figueirense Esporte Clube')

print('=-=' * 15)
print(f'Lista de times {times}')
print('=-=' * 15)

print('=-=' * 15)
print(f'Os 5 primeiros colocados são: {times[0:5]}')
print('=-=' * 15)

print('=-=' * 15)
print(f'Os 4 últimos colocados são: {times[-4:]}')
print('=-=' * 15)

print('=-=' * 15)
print(sorted(times))
print('=-=' * 15)

print('=-=' * 15)
print(f'Times em ordem alfabética: {sorted(times)}')
print('=-=' * 15)

print('=-=' * 15)
print(f'O Galo está na {times.index("Clube Atlético Mineiro")+1}ª posição')
print('=-=' * 15)