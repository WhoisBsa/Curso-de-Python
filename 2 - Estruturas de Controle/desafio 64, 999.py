"""
Crie um programa que leia vários números inteiros pelo teclado. O programa
só para quando digitar 999. No final mostre quantos números foram digitados
e qual foi a soma entre eles
"""

soma = 0
while True:
    n = int(input('Digite um número [999 para sair]: '))
    if n == 999:
        break
    else:
        soma += 1
print('O total de números digitados foi: {}'.format(soma))
print('FIM')