"""
Desenvolva um programa que leia quatro valores pelo teclado e guarde-os
em um tupla. No final, mostre:
A - Quantas vezes apareceu o valor 9;
B - Em que posição foi digitado o primeiro valor 3;
C - Quais foram os números pares.
"""

n = (int(input('1º numero: ')), int(input('2º numero: ')),
     int(input('3º numero: ')), int(input('4º numero: ')))

print(f'Voce digitou os valores {n}')

print(f'O numero 9 apareceu {n.count(9)} vezes')

if 3 in n:
    print(f'O numero 3 foi digitado na posiçao {n.index(3)+1}')
else:
    print('O número 3 não está nessa sequencia')

print('O números pares dessa sequencia são: ', end='')
for i in n:
      if i%2 == 0:
          print(i, end=' ')
