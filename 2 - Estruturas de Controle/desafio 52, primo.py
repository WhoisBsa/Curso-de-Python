"""
Faça um programa que leia um numero e diga se ele é primo
"""

n = int(input('Digite um numero: '))
c = 0

for i in range(1, n+1):
    if n % i == 0:
        c += 1
        print('\033[33m{}'.format(i), end=' ')
    else:
        print('\033[31m{}'.format(i), end=' ')
print('\n\033[mO numero {} foi divisivel {} vezes, portanto ele'
      .format(n, c), 'é um numero primo' if c <= 2 else 'não é um numero primo')
