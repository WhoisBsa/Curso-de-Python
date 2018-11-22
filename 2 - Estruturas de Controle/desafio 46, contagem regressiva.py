"""
Faça um programa que mostre na tela uma contagem regressiva para o estouro
de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles
"""

from time import sleep
import emoji

for i in range(10, 0, -1):
    print(i)
    sleep(0.3)
print(emoji.emojize(':boom:'*3, use_aliases=True))
