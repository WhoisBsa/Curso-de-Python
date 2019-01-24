"""
Crie um programa que leia nome, sexo e idade de várias pressoas,
guardando os dados em um dicionário e todos os dicionários em uma
lista. No final, mostre:
A - Quantas pessoas foram cadastradas.
B - A média de idade do grupo.
C - Uma lista com todas as mulheres.
D - Uma lista com todas as pessoas com idade acima da média.
"""


import math

pessoa = dict()
pessoas = list()
media = 0

while True:
    pessoa['nome'] = str(input('Nome: '))
    pessoa['sexo'] = str(input('Sexo [M/F]: ')).upper().strip()
    pessoa['idade'] = int(input('Idade: '))

    # Valida o resultado de sexo apenas pra M ou F
    while pessoa['sexo'] not in 'MF':
        print('Apenas \033[31m[M/F]\033[m tente novamente')
        pessoa['sexo'] = str(input('Sexo : ')).upper().strip()

    # Adiciona todas as pessoas na lista pessoas
    pessoas.append(pessoa.copy())

    media += pessoa['idade']

    # Opcao de continuar ou parar o while
    op = str(input('Quer continuar? [S/N] ')).upper().strip()
    while op not in 'SN':
        print('Apenas S/N, tente novamente. ')
        op = str(input('Quer continuar? \033[31m[S/N]\033[m ')).upper().strip()
    if op in 'N':
        print('=-=' * 15)
        break

print(f'- O grupo tem {len(pessoas)} pessoas.')
print(f'- A média de idade é de {math.ceil(media/len(pessoas))} anos.')
print(f'- As mulheres cadastradas foram:', end='')
for p in pessoas:
    if p['sexo'] == 'F':
        print(f'{p["nome"]}', end=' ')
print()
print('- Lista de pessoas que estão acima da média:')
for p in pessoas:
    if p['idade'] > media/len(pessoas):
        for k, v in p.items():
            print(f'{" ":>5} {k}: {v}', end='')
    print()

print('<'*8, 'Fim do programa', '>'*8)
