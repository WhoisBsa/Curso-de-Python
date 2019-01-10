"""
Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear 6
números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
"""

from random import randint
from time import sleep

jogos = int(input('Quantos jogos deseja fazer? '))
numeros = 0
jogosmega = [[]] * jogos




for i in range(0, jogos):
    for j in range(0, 6):
        numeros = randint(1, 61)
        if numeros not in jogosmega:
            jogosmega[i].append(numeros)






for posicao, valores in enumerate(jogosmega):
    print(f'{posicao+1}º jogo: {valores}')
    sleep(1)
