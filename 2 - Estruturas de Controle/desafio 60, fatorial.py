"""
Faça um programa que leia um numero qualquer e mostre o seu fatorial
"""

'''import math

n = int(input('Digite um número: '))
fat = math.factorial(n)
print('{}! = {}'.format(n,fat))'''

n = int(input('Digite um número: '))
c = n
fat = 1

print('{}! = '.format(n), end='')
while c > 0:
    print('{} '.format(c), end='')
    print('x ' if c > 1 else '= ', end='')
    fat *= c
    c -= 1

print('{}'.format(fat))

