"""
Crie um programa que vai gerar cinco números aleatórios e colocar
em uma tupla.
Depois disso, mostre a listagem de números gerados e tambem indique o
menos e o maior valor que estão na tupla
"""

from random import randint

numeros = (randint(1, 100), randint(1, 100), randint(1, 100),
     randint(1, 100), randint(1, 100))

print('Os números sorteados foram: ', end='')
for n in numeros:
    print(f'{n} ', end='')

print(f'\nO maior valor é {max(numeros)} e o menor é {min(numeros)}')