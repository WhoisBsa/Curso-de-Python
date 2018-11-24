"""
Desenvolva um programa que leia o nome, idadde e sexo de 4 pessoas.
No final do programa, mostre:
- A média de idade do grupo.
- Qual é o nome do homem mais velho.
- Quantas mulheres tem menos de 20 anos.
"""

somaidade = maior = cont = m20 = 0

#achar o homem mais velho
hmaisvelho = ''
ihmaisvelho = 0
ficha = list()

while cont < 4:
    print('-' * 5, end=' ')
    print('{}ª Pessoa'.format(cont+1), end=' ')
    print('-' * 5)
    n = str(input('Nome: ')).strip()
    i = int(input('Idade: '))
    s = str(input('Sexo [M/F]: ')).strip()

    #verifica quem é o homem mais velho
    maior = i
    if i > maior and s in 'Mm':
        maior = i


    #salva a idade e o nome do mais velho
    if s in 'Mm' and i == maior:
        hmaisvelho = n
        ihmaisvelho = i

    #verifica quais mulheres tem menos de 20 anos
    if s in 'Ff' and i < 20:
        m20 += 1

    #faz a soma das idades
    somaidade += i

    cont += 1

media = somaidade/4
print('\nResultados:')
print('A média de todos os integrantes é de {}'.format(media))
print('O homem mais velho tem {} e seu nome é {}'.format(ihmaisvelho, hmaisvelho))
print('Existem {} mulheres com menos de 20 anos'.format(m20))


