"""
Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada
valor digitado pelo usuário. O programa será interrompido quando o número solicitado
for negativo.
"""

n = 0
while True:
    n = int(input('Informe o valor: '))
    if n < 0:
        break
    print('A tabuada é')
    print('-=' * 11)
    for i in range(0, 11):
        print('{} * {} = {}'.format(n, i, n * i))
    print('-=' * 11)