"""
Faça um programa que leai seis números inteiros e mostre a soma apenas daqueles
que forem pares. Se o valor digitado for impar, desconsidere-o
"""

from random import randint

n = [0]*6
soma = 0

print('Vetor: ', end=' ')
for i in range(0, 6):
    n[i] = randint(0, 10)
    print(n[i], end=' ')
    if n[i] % 2 == 0:
        soma += n[i]
print('\nA soma dos números pares é: {}'.format(soma))
