"""
Faça um programa que faça o computador jogar jokenpô com você
"""

from random import choice

PPT = ('PEDRA', 'PAPEL', 'TESOURA')

condicao = True
while condicao:
    escolhadopc = choice(PPT)
    suaescolha = str(input('Escolha (Pedra, Papel ou Tesoura): ')).upper().strip()

    if suaescolha in PPT:
        print('Sua escolha foi {} e a do computador foi {}, o resultado foi que '.format(suaescolha, escolhadopc), end='')

        if escolhadopc == suaescolha:
            print('houve empate')

        elif escolhadopc == 'PEDRA' and suaescolha == 'TESOURA':
            print('o computador venceu')

        elif escolhadopc == 'TESOURA' and suaescolha == 'PAPEL':
            print('o computador venceu')

        elif escolhadopc == 'PAPEL' and suaescolha == 'PEDRA':
            print('o computador venceu')

        elif escolhadopc == 'TESOURA' and suaescolha == 'PEDRA':
            print('você venceu')

        elif escolhadopc == 'PAPEL' and suaescolha == 'TESOURA':
            print('você venceu')

        elif escolhadopc == 'PEDRA' and suaescolha == 'PAPEL':
            print('você venceu')

        else:
            print('essa não é uma opção válida')
    else:
        print('Obrigado por jogar, volte sempre!')
        condicao = False
        break
