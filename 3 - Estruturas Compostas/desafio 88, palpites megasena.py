"""
Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear 6
números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
"""

from random import randint
from time import sleep


print("""=-=-=-=-=-=-=\n  MEGA SENA  \n=-=-=-=-=-=-=""")

lista = list()
jogosmega = list()
jogos = int(input('Quantos jogos deseja fazer? '))
tot = 1

while tot <= jogos:
    cont = 0
    while True:
        numeros = randint(1, 60)
        if numeros not in jogosmega:
            lista.append(numeros)
            cont += 1
        if cont >= 6:
           break
    lista.sort()
    jogosmega.append(lista[:])
    lista.clear()
    tot += 1

for posicao, valores in enumerate(jogosmega):
    print(f'{posicao+1}º jogo: {valores}')
    sleep(1)
