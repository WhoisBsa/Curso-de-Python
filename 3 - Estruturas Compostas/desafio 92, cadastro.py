"""
Crie um programa que leia nome, ano de nascimento e carteira de trabalho
e cadastre-os (com idade) em um dicionário, se por acados a CTPS for
diferente de zer, o dicionário receberá também o ano de contratação e o
salário. Calcule e acrescente, além da idade, com quantos anos a pessoas
vai se aposentar.
"""

from datetime import date

cadastro = dict()
nascimento = 0

cadastro['nome'] = str(input('Nome: '))
nascimento = int(input('Ano de Nascimento: '))
cadastro['idade'] = date.today().year - nascimento
cadastro['ctps'] = int(input('Carteira de Trabalho (0 não tem) '))
if cadastro['ctps'] != 0:
    cadastro['contratacao'] = int(input('Ano de Contratação: '))
    cadastro['salario'] = int(input('Salário: '))
    cadastro['aposentadoria'] = (cadastro['contratacao'] + 35) - nascimento
print('=-=' * 11)

for k, v in cadastro.items():
    print(f'{k}: {v}')

