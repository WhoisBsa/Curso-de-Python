"""
Faça um programa que leia o ano de nascimento de um jovem e informe,
de acordo com sua idade:
    - Se ele ainda vai se alistar ao serviço militar.
    - Se é a hora de se alistar.
    - Se já passou do tempo de alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
"""

idade = int(input('Informe sua idade: '))

if idade == 18:
    print('É hora de se alistar')
elif idade < 18:
    print('Não é a hora de se alistar ainda')
    print('Falta {} anos pra você se alistar'.format(18 - idade))
elif idade > 18:
    print('Já passou da hora de você se alistar')
    print('Já se passou {} anos do prazo pra você se alistar'.format(idade - 18))