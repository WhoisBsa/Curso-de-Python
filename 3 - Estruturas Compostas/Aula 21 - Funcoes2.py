help(print)
print(input.__doc__)


def contador(i, f, p):
	"""
	-> Faz uma contagem e mostra na tela.
	"""
	c = i
	while c <= f:
		print(f'{c}', end='... ')
		c += p
	print('fim')


contador(2, 10, 2)
help(contador)


def somar(a=0, b=0, c=0):
	s = a + b + c
	print(s)


somar(3, 2, 5)
somar(8, 4)
somar()


def teste():
	x = 8
	print(f'Na funcao teste, n vale {n}')
	print(f'Na funcao teste, x vale {x}')


#Programa principal
n = 2
print(f'No programa principal, n vale {2}')
teste()
#print(f'No programa pruncipal, x vale {x}')


#Return

def somar(a=0, b=0, c=0):
	s = a + b + c
	return s


r1 = somar(2, 4, 6)
r2 = somar(2, 3)
r3 = somar()

print(f'Os resultados foram {r1} {r2} {r3}')


def fatorial(num=1):
	if num == 0:
		return 1
	else:
		return num * fatorial(num-1)

n = 5
print(fatorial(n))

