"""
A Comfederação Nacional de Natação precisa de um programa que leia o ano de nascimento
de um atleta e mostre sua categoria, de acordo com a idade:
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JUNIOR
- Até 20 anos: SÊNIOR
- Acima: MASTER
"""

from datetime import date

condition = True

while (condition):
    ano = int(input('Informe o ano de nascimento (0 para sair): '))
    if ano == 0:
        condition = False
        break
    if date.today().year - ano <= 9:
        print('CATEGORIA MIRIM\n ')
    elif date.today().year - ano > 9 and date.today().year - ano <= 14:
        print('CATEGORIA INFANTIL\n')
    elif date.today().year - ano > 14 and date.today().year - ano <= 19:
        print('CATEGORIA JUNIOR\n')
    elif date.today().year - ano > 19 and date.today().year - ano < 25:
        print('CATEGORIA SÊNIOR\n')
    elif date.today().year - ano > 25:
        print('CATEGORIA MASTER\n')
