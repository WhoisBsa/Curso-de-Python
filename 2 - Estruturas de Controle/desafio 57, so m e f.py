"""
Faça um programa que leia o sexo de uma pessoa, mas só aceite M ou F.
Caso esteja errado, repita
"""

sexo = str(input('Digite seu sexo [M/F]: ')).strip()[0]
while sexo not in 'FfMm':
    sexo = str(input('Valor errado digite seu sexo novamente: ')).strip()[0]

print('PRONTO')