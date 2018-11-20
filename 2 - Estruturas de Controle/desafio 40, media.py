"""
Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando
um mensagem no final, de acordo com a média atingida:
- Média abaixo de 5.0: Reprovado
- Média entre 5.0 e 6.9: Recuperação
- Média acima de 7.0: Aprovado
"""

n1 = int(input('Nota 1: '))
n2 = int(input('Nota 2: '))
media = float((n1 + n2)/2)
print(f'A média de {n1} e {n2} é {media}')
if media < 5.0:
    print('Reprovado')
elif media >= 5.0 and media < 7:
    print('Recuperação')
else:
    print('Aprovado')