"""
Crie um programa que leia vários números inteiros pelo teclado.
No final mostre a média e o maior e menor valor. Perguntar se quer
continuar a digitar os valores
"""

soma = 0
total = 0
maior = menor = 0
while True:
    n = int(input('Digite um número: '))
    soma += n
    total += 1
    media = soma / total
    if total == 1:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n

    continuar = str(input('Deseja continuar? [S/N]: ')).upper().strip()
    if continuar not in 'S':
        break

print('A média dos números digitados foi: {:.2f}'.format(media))
print('O maior número é {} e o menor é {}'.format(maior, menor))
print('FIM')
