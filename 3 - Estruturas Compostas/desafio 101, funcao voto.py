"""
Crie um programa que tenha uma funcao chamada voto() que vai receber
como parametro o ano de nascimento de uma pessoa, retornando um valor 
literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGAGORIO
nas eleicoes
"""


def voto(ano):
	"""
	Funcao que recebe o ano de nascimento e verifica se a pessoa
	pode votar ou nao
	"""
	from datetime import date
	
	#idade recebe o ano atual menos o ano de nascimento
	idade = date.today().year - ano
	
	print(f'Com {idade} anos: Voto', end=' ')
	if idade < 16:
		return 'Negado'
	elif 16 <= idade < 18 or idade > 65:
		return 'Opcional'
	else:
		return 'Obrigatorio'
		
		
print('=-=' * 10)
anoNasc = int(input('Ano de nascimento: '))
print(voto(anoNasc))
print('=-=' * 10)
