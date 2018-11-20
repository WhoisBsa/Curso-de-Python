"""
Escreva um programa que leia um número inteiro qualquer e peça paro o
usuário escolher qual será sua base de conversão:
- 1 para binário
- 2 para octal
- 3 pra hexadecimal
"""

n = int(input('Digite o número: '))
print('Qual base voce deseja converter')
print('''[1] para binário
[2] para octal 
[3] pra hexadecimal''')
base = int(input('Base: '))

if base == 1:
    print('{} convertido para binário é igual a {}'.format(n, bin(n)[2:]))
elif base == 2:
    print('{} convertido para binário é igual a {}'.format(n, oct(n)[2:]))
elif base == 3:
    print('{} convertido para binário é igual a {}'.format(n, hex(n)[2:]))
else:
    print('Valor inválido')
