"""
Faça um programa que leia nome e média de um aluno,
guardando também a situação em um dicionário. No final,
mostre o conteúdo da estrutura na tela.
"""


aluno = dict()

aluno['nome'] = str(input('Nome: '))
aluno['nota'] = int(input(f'Média de {aluno["nome"]}: '))
media = aluno['nota']
aluno['situacao'] = 'Aprovado' if media >= 7 else 'Reprovado'

for k, v in aluno.items():
    print(f'{k} é igual a {v}')
