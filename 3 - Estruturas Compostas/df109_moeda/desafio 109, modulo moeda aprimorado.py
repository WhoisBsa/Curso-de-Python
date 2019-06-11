"""
Modifique as funções que foram cridas no desafio 107 para que elas aceitem
um parâmetro a mais, informando se o valor retornado por elas vai ser ou não
formatado pela função moeda(), desenvolvida no desafio 108.
"""


from df109_moeda import moeda

price = float(input('Price: R$'))
print(f'The double of {moeda.moeda(price)} is {moeda.double(price, True)}')
print(f'The half of {moeda.moeda(price)} is {moeda.half(price, True)}')
print(f'The plus of 10% of {moeda.moeda(price)} is {moeda.plus(price, 10, False)}')
print(f'The decrease of 40% of {moeda.moeda(price)} is {moeda.decrease(price, 40, True)}')
