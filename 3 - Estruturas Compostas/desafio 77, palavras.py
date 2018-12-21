"""
Crie um programa que tenha uma tupla com várias palavras.
Depois disso, você deve mostrar, para cada palavra, quais são
as suas vogais.
"""

palavras = ('codigo', 'estudo', 'computador', 'python', 'programador')

for i in palavras:
    print(f'Na palavra {i} temos', end='')
    for letra in i:
        if letra in 'aeiou':
            print(letra, end=' ')
    print('\n')
