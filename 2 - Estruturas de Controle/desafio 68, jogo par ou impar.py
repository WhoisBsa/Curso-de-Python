"""
Faça um programa que jogue par ou ímpar com o computador. O jogo
só será interrompido quando o jogador PERDER, mostrando o total de
vitórias consecutivas que ele conquistou no final do jogo
"""

import random

print('=-=' * 8)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-=' * 8)

valorUser = int(input('Digite um valor: '))
pi = str(input('Par ou Ímpar? [P/I] ')).strip().upper()
cont = 0

while True:
    # Escolhe aleatóriamente um valor entre 0 e 10
    valorPc = random.randrange(0, 10)

    # Soma os valores do usuário de da máquina para apurar os resultados
    soma = valorUser + valorPc
    print('-=-' * 8)
    print(f'Você jogou {valorUser} e o computador {valorPc}. Total de {soma} deu ', end='')

    # Valida se os resultados foram pares ou ímpares
    if soma%2 == 0:
        print('PAR')
    else:
        print('ÍMPAR')
    print('-=-' * 8)

    # Verifica se o usuário ganhou ou perdeu
    # Se ganhar o usuário tem mais uma chance
    if soma%2 == 0 and pi == 'P':
        cont += 1
        print('Você VENCEU!')
        print('Vamos jogar novamente...')
        print('-' * 8)
        valorUser = int(input('Digite um valor: '))
        pi = str(input('Par ou Ímpar? [P/I] ')).strip().upper()

    elif soma%2 != 0 and pi == 'I':
        cont += 1
        print('Você VENCEU!')
        print('Vamos jogar novamente...')
        print('-' * 8)
        valorUser = int(input('Digite um valor: '))
        pi = str(input('Par ou Ímpar? [P/I] ')).strip().upper()

    else:
        print('Você PERDEU')
        print('-=-' * 8)
        break

print(f'GAME OVER! Você venceu {cont} vezes')