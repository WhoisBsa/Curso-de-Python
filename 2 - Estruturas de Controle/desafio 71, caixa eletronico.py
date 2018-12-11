"""
Crie um programa que simule o funcionamento de um caixa eletrônico.
No início, pergunte ao usuário qual será o valor a ser sacado e o
programa vai informar quantas cédulas de cada valor serão entregues.

OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
"""

print("""=-=-=-=-$-$-=-=-=-=\n=-$  BANCO MBS  $-=\n=-=-=-=-$-$-=-=-=-=""")

saque = int(input('Qual valor você deseja sacar? R$'))

# Notas disponíveis para saque
notade1 = 1
notade10 = 10
notade20 = 20
notade50 = 50
cont1 = cont10 = cont20 = cont50 = 0

while True:
    # Verifica quantas notas serão necessárias para igualar o valor do saque a zero.
    if saque >= 50:
        saque -= notade50
        cont50 += 1
    elif saque >= 20 and saque < 50:
        saque -= notade20
        cont20 += 1
    elif saque >= 10 and saque < 20:
        saque -= notade10
        cont10 += 1
    elif saque >= 1 and saque < 10:
        saque -= notade1
        cont1 += 1
    else:
        break

if cont50 > 0:
    print(f'Total de {cont50} cédulas de R$50')
if cont20 > 0:
    print(f'Total de {cont20} cédulas de R$20')
if cont10 > 0:
    print(f'Total de {cont10} cédulas de R$10')
if cont1 > 0:
    print(f'Total de {cont1} cédulas de R$1')
print('=' * 44)
print('Volte sempre ao BANCO MBS! Tenha um bom dia!')
print('=' * 44)
