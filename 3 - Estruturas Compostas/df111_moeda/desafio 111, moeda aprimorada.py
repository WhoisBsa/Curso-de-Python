"""
Crie um pacote chamado utilidadesCev que tenha dois módulos internos chamados
moeda e dado.

Transfira todas as funções utilizadas nos desafios 107, 108 e 109
para o primeiro pacote e matenha o tudo funcionando.
"""

from df111_moeda import moeda

price = float(input('Price: R$'))
moeda.resumo(price, 10, 40)
