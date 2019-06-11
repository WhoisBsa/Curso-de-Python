"""
Adapte o código do desafio 107, criando uma função adicional chamada
moeda() que consiga mostrar os valores como um valor monetário formatado.
"""

from df108_moeda import moeda

price = float(input('Price: R$'))
print(f'The double of {moeda.moeda(price)} is {moeda.moeda(moeda.double(price))}')
print(f'The half of {moeda.moeda(price)} is {moeda.moeda(moeda.half(price))}')
print(f'The plus of 10% of {moeda.moeda(price)} is {moeda.moeda(moeda.plus(price, 10))}')
print(f'The decrease of 40% of {moeda.moeda(price)} is {moeda.moeda(moeda.decrease(price, 40))}')
