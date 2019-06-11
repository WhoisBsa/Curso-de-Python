"""
Dentro do pacote utilidadesCev que criamos no desafio 111, temos
um módulo chamado dado. Crie uma função chamada leiaDinheiro()
que seja capaz de funcionar como a função input(), mas com uma
validação de dados para aceitar apenas valores que sejam monetários.
"""

from df112_moeda import moeda
from df112_moeda import dado

price = dado.read_money('Price: R$')
moeda.resumo(price, 10, 40)
