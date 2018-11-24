"""
Crie um programa que leia dois valores e mostre um menu na tela:
1 - Somar
2 - Multiplicar
3 - Maior
4 - Novos numeros
5 - Sair
"""

while True:
    n1 = int(input('Digite o primeiro valor: '))
    n2 = int(input('Digite o segundo valor: '))
    op = int(input("""O que voce deseja fazer
1 - Somar
2 - Multiplicar
3 - Maior
4 - Novos numeros
5 - Sair
Escolha uma opção: """))
    if op > 5 or op < 1:
        print('Opção inválida, tente novamente\n')
    else:
        if op == 1:
            print('Soma entre {} e {} é: {}'.format(n1, n2, n1 + n2))
            break
        elif op == 2:
            print('Multiplicação entre {} e {} é: {}'.format(n1, n2, n1 * n2))
            break
        elif op == 3:
            if n1 > n2:
                print('Maior número entre {} e {} é: {}'.format(n1, n2, n1))
                break
            else:
                print('Maior número entre {} e {} é: {}'.format(n1, n2, n2))
                break
        elif op == 4:
            print('')
        else:
            print('-'*10, 'FIM', '-'*10)
            break
