"""
Melhore o jogo do desafio 028 onde o computador vai "pensar" em um número entre 0 e 10.
Só que agora o jogador vai adivinhar até acertar, mostrando quantos palpites fez
"""

import random

n = random.randrange(1, 6)
tentativas = 0

while True:
    chance = int(input('Escolha (1 a 5): '))
    tentativas += 1
    if chance == n:
        print('Uhul, ganhou')
        break
    else:
        print('Loser')
print('Voce precisou de {} tentativas para ganhar'.format(tentativas))