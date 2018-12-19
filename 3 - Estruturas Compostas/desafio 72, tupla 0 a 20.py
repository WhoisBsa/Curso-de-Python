"""
Crie um programa que tenha um tupla totalmente preenchida com uma contagem
por extenso, de zero até vinte.
Seu programa deverá ler um número pelo teclado e mostrá-lo por extenso.
"""

extenso = ('zero', 'um', 'dois',
           'três', 'quatro', 'cinco',
           'seis', 'sete', 'oito',
           'nove', 'dez', 'onze',
           'doze', 'treze', 'quatorze',
           'quinze', 'dezesseis', 'dezessete',
           'dezoito', 'dezenove', 'vinte')

# Assegurar que o valor esteja entre 0 e 20
while True:
    n = int(input('Digite um número entre 0 e 20: '))
    if 0 <= n <= 20:
        break
    print('Valor inválido!')

print(f'Você escolheu o número {extenso[n]}')