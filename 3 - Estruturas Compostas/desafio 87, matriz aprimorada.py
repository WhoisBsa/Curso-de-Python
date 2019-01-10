"""
Aprimore o desafio anterior, mostrando no final:
A - A soma de todos os valores pares digitados.
B - A soma dos valores da terceira coluna.
C - O maior valor da segunda linha.
"""



matriz = [[], [], []]
valor = 0
soma = soma3 = maior1 = 0

for i in range(0, 3):
    for j in range(0, 3):
        valor = int(input(f'Digite o valor para [{i}][{j}]: '))
        matriz[i].append(valor)

print('=-=' * 15)

for i in matriz[0]:
    print(f'[ {i} ]', end=' ')
    if i % 2 == 0:
        soma += i
print()
for i in matriz[1]:
    print(f'[ {i} ]', end= ' ')
    if i % 2 == 0:
        soma += i
    if len(matriz) == 0:
        maior1 = i
    else:
        if i > maior1:
            maior1 = i
print()
for i in matriz[2]:
    print(f'[ {i} ]', end=' ')
    if i % 2 == 0:
        soma += i
    soma3 += i
print()
print('=-=' * 15)
print(f'A soma de todos os valores pares é igual a {soma}')
print(f'A soma dos valores da 3º coluna é igual a {soma3}')
print(f'O maior valor da 2º coluna é igual a {maior1}')