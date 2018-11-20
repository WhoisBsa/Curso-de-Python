"""
Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior, os dois são iguais
"""

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))

if n1 > n2:
    print('\033[1;34m{}\033[m é maior que \033[1;31m{}'.format(n1, n2))
elif n1 < n2:
    print('\033[1;34m{}\033[m é maior que \033[1;31m{}'.format(n2, n1))
else:
    print('\033[1;34m{}\033[m é maior que \033[1;31m{}'.format(n1, n2))
