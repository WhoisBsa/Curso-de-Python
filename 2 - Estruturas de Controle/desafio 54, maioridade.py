"""
Crie um programa que leia o ano de nascimento de sete pessoas.
No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já
são maiores
"""

from datetime import date

nMaioridade = 0
for i in range(1, 3):
    ano = int(input('Digite o ano de seu nascimento: '))
    if date.today().year - ano < 18:
        nMaioridade += 1
print(date.today().year)
if nMaioridade == 1:
    print('{} pessoas ainda nao atingiu a maioridade'.format(nMaioridade))
else:
    print('{} pessoas ainda nao atingiram a maioridade'.format(nMaioridade))