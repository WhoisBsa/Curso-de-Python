"""
Faça um programa que leia 5 valores numéricos e guardo-os numa em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas respec-
tivas posições na lista.
"""

valores = list()
for i in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
print(f'Você digitou os valores {valores}')

print(f'O maior valor foi {max(valores)} na posição {valores.index(max(valores))}')
print(f'O menor valor foi {min(valores)} na posição {valores.index(min(valores))}')