"""
Melhore o desafio 61, perguntar para o usuario se ele quer mostrar mais
alguns termos. Encerra com 0
"""

print('-'*5, 'Gerador de PA', '-'*5)
p = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razao da sua PA: '))
termo = p
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print('{}'.format(termo), end=' - ')
        termo += r
        cont += 1
    print('Pausa')
    mais = int(input('\nQuantos termos a mais [0 para sair]: '))
print('Progreção finalizada com {} termos'.format(total))

