"""
Faça um programa que tenha uma funcao chamada 
area(), que receba
as dimensoes de um terreno retangular (largura e 
comprimento) e mostre 
a area do terremo.
"""


def area(l, c):
    a = l * c
    print(f'A area do terreno é de {a} metros quadrados')

largura = int(input('Largura do terreno: '))
comprimento = int(input('Comprimento do terreno: '))
area(largura, comprimento)

