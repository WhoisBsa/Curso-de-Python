"""
Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada,
o  programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
A - Quantas pessoas tem mais de 18 anos.
B - Quantos homens foram cadastrados.
C - Quantas mulheres tem menos de 20 anos.
"""

contMaior18 = 0
contHomens = 0
contMMenor20 = 0

while True:
    print('=-=' * 8)
    print('CADASTRE UMA PESSOA')
    print('=-=' * 8)
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    # Valida a escolha do sexo
    while sexo not in 'MmFf':
        sexo = str(input('Só é valido M ou F. Tente novamente: ')).strip().upper()

    # Conta o número de pessoas que se enquadram em cada condição
    if idade > 17:
        contMaior18 += 1
    if sexo == 'M':
        contHomens += 1
    if idade < 21 and sexo == 'F':
        contMMenor20 += 1

    # Pergunta ao usuário se ele quer continuar, enquanto não for
    # S ou N o programa não para de perguntar
    print('-' * 24)
    op = ' '
    while op not in 'SsNn':
        op = str(input('Quer continuar? [S/N] ')).strip().upper()

    if op in 'Nn':
        print('-' * 24)
        break
print(f'Total de pessoas com mais de 18 anos: {contMaior18}')
print(f'Total de homens cadastrados: {contHomens}')
print(f'Total de mulheres menores de 20 anos: {contMMenor20}')