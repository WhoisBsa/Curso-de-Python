"""
Faça um programa que leia o peso de cinco pessoas.No final, mostre
qual foi o maior e o menor peso lidos
"""


maior = menor = 0

for i in range(1, 6):
    peso = float(input('{} - peso: '.format(i)))

    if i == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print('O maior peso é {}kg e o menor é {}kg'.format(maior, menor))
