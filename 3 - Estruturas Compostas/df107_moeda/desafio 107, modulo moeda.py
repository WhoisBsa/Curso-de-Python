"""
Crie um módulo chamado moeda.py que tenha as funções incorporadas
aumentar(), diminuir(), dobro() e metade().

Faça também um programa que importe esse módulo e use algumas dessas funções.
"""

from df107_moeda import moeda

price = float(input('Price: R$'))
print(f'The double of the price is {moeda.double(price)}')
print(f'The half of the price is {moeda.half(price)}')
print(f'The plus of 10% of the price is {moeda.plus(price, 10)}')
print(f'The decrease of 40% of the price is {moeda.decrease(price, 40)}')
