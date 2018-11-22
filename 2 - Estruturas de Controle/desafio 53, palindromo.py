"""
Faça um programa que leia uma frase e difa se ela é um palindromo
"""

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''

print('A frase {}'.format(frase), end=' ')

for letra in range(len(junto) - 1, -1, -1): #vai até antes da primeira letra de trás pra frente
    inverso += junto[letra]
if junto == inverso:
    print('é um palindromo')
else:
    print('não é um palindromo')
