"""
Crie um programa que tenha uma funcao fatorial() 
que receba dois parametros: o primeiro que 
indique o numero a calcular e o outro chamado
show, que sera um valor logico indicando se 
sera mostrado ou nao na tela o processo de 
calculo do fatorial
"""

def fatorial(num=1, show=False): 
	for n in range(num, 0, -1):
		if show:
			print(n, end='')
			if n > 1:
				print(' x ', end='')
			else:
				print(' = ', end='')
	if num == 0:
		return 1 
	else:
		return num * fatorial(num-1)

                 
print(fatorial(5, show=True))
