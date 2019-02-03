"""
Faca um programa que tenha uma funcao chamada contador(), que receba 
tres parametros: inicio, fim e passo e realize a contagem.
Seu programa tem qua realizar tres contagens atraves da funcao criada:
A - De 1 ate 10, de 1 em 1;
B - De 10 ate 0, de 2 em 2;
C - uma contagem personalizada.
"""

from time import sleep


def contador(inicio, fim, passo):
	if passo == 0:
		passo = 1
	if passo < 0:
		passo *= -1
	print('=-=' * 10)
	print(f'Contagem de {inicio} até {fim} de {passo} em {passo}:')
	if inicio < fim:
		for i in range(inicio, fim + 1, passo):
			print(i, end=' ', flush=True)
			sleep(0.5)
		print('FIM!')
	else:
		for i in range(inicio, fim - 1, -passo):
			print(i, end=' ', flush=True)
			sleep(0.5)
		print('FIM!')


#Contagens pre-definidas
contador(1, 10, 1)
contador(10, 0, 2)

#Contagem personalizada pelo usuario
print('=-=' * 10)
print('Personalize a contagem')
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)
