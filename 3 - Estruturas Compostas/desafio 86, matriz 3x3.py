"""
Crie um programa que crie uma matriz de dimensão
3x3 e preencha com valores lidos pelo teclado.
No final, mostra a matriz na tela, com a formatação correta.
"""

matriz = [[], [], []]
valor = 0

for i in range(0, 3):
    for j in range(0, 3):
        valor = int(input(f'Digite o valor para [{i}][{j}]: '))
        matriz[i].append(valor)

for i in matriz[0]:
    print(f'[ {i} ]', end=' ')
print()
for i in matriz[1]:
    print(f'[ {i} ]', end= ' ')
print()
for i in matriz[2]:
    print(f'[ {i} ]', end=' ')
