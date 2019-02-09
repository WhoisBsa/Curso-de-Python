"""
faca um programa que tenha uma funca chamada ficha(), que receba dois parametros 
opcionais: o nome de um jogador e quantos gols ele marcou.
O programa devera ser capz de mostrar a ficha do jogador, mesmo que algum dado nao 
tenha sido informado corretamente.
"""


def ficha(n, g):
    print(f'O jogador {n} fez {g} gol(s) no campeonato')


nome = str(input('Nome do jogador: '))
gols = str(input('Gols: '))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome.strip() == '':
    nome = '<desconhecido>'

ficha(nome, gols)
