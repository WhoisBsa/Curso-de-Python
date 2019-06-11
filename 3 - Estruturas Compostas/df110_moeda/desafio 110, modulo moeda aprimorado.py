"""
Adicione ao módulo moeda.py criado nos desafios anteriores, uma função chamada
resumo(), que mostre na tela algumas informações geradas pelas funções que já
temos no módulo criado até aqui.
"""


from df110_moeda import moeda

price = float(input('Price: R$'))
moeda.resumo(price, 10, 40)
