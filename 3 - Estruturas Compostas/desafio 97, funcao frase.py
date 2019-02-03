"""
Faca um programa que tenha uma funcao chamada escreva(), que receba 
um texto qualquer como parametro e mostre uma mensagem com tamanho 
adaptavel
"""


def escreva(frase):
	print('~' * (len(frase) + 4))
	print(f'  {frase}')
	print('~' * (len(frase) + 4))


escreva('Matheus Barbosa')
escreva('Python')
escreva('CEV')
