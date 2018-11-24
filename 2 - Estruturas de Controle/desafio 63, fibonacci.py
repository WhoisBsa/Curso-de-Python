"""
Escreva um programa que leia um número n inteiro qualquer e mostre na tela
os n primeiros elementos de uma Sequência de Fibonacci
"""

print('-'*5, 'Sequência de Fibonacci', '-'*5)
fib = int(input('Quantos números da sequencia: '))
t1 = 0
t2 = 1
print('{} - {} - '.format(t1, t2), end='')

cont = 3
while cont <= fib:
    t3 = t1 + t2
    t1 = t2
    t2 = t3
    print('{} - '.format(t3), end='')
    cont += 1
print('FIM')
