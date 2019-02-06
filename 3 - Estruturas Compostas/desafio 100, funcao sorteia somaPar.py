"""
Faca um programa que tenha uma lista chamada 
numeros e duas funcoes 
chamadas sortei() e somaPar(). A primeira funcao 
vai sortear 5 numeros e vai 
colocar dentro da lista e a segunda funcao vai 
mostrar a soma entre todos os 
valores pares sorteados pela funcao anterior
"""

from random import randint
from time import sleep


numeros = []
soma = 0

def sorteia(numeros):
	''' Funcao de sortear numeros na lista '''
	numeros = [randint(0,10), randint(0,10), 
	randint(0,10), randint(0,10), randint(0,10)]
	return numeros


def somaPar(numeros, soma):
	''' Funcao de somar os numeros pares da lista '''
	for i in numeros:
		if i % 2 == 0:
			soma += i
	return soma

#recebe os numeros sorteados na funcao
numeros = sorteia(numeros)
#mostra os valores a cada 0.5 segundos
print('Os numeros sorteados sao:')
for i in numeros:
	print(i, end=' ', flush=True)
	sleep(0.5)
print() #pula uma linha
#recebe a soma de numeros pares
soma = somaPar(numeros, soma)
print(f'A soma de numeros pares da lista e de {soma}.')
