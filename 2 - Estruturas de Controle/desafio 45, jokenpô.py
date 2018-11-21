"""
Faça um programa que faça o computador jogar jokenpô com você
"""

from random import choice

PPT = ('Pedra', 'Papel', 'Tesoura')

condicao = True
while condicao:
    escolhadopc = choice(PPT)
    suaescolha = str(input('Escolha (Pedra, Papel ou Tesoura): '))
    if suaescolha in PPT:
        print('Sua escolha foi {} e a do computador foi {}, o resultado foi que '.format(suaescolha, escolhadopc), end='')
        if escolhadopc == suaescolha:
            print('houve empate')
        elif escolhadopc == 'Pedra' and suaescolha == 'Tesoura':
            print('o computador venceu')
        elif escolhadopc == 'Tesoura' and suaescolha == 'Papel':
            print('o computador venceu')
        elif escolhadopc == 'Tesoura' and suaescolha == 'Pedra':
            print('você venceu')
        elif escolhadopc == 'Papel' and suaescolha == 'Tesoura':
            print('você venceu')
        elif escolhadopc == 'Pedra' and suaescolha == 'Papel':
            print('você venceu')
        elif escolhadopc == 'Papel' and suaescolha == 'Pedra':
            print('o computador venceu')
        else:
            print('essa não é uma opção válida')
    else:
        print('Obrigado por jogar, volte sempre!')
        condicao = False
        break