"""
Crie um programa que tenha a funcao leiaint(), que vai funcionar 
de forma semelhante à input() do pythin, so que fazendo a validacao 
para aceitar apenas um valor numerico
"""


def leiaint(msg):
	n = str(input(msg))
	while not n.isnumeric():
		n = input(f'\033[31;3m Erro, apenas numeros inteiros: \033[m')
	return n

n = leiaint('Digite um numero: ')
print(f'Voce acabou de digitar o numero {n}')