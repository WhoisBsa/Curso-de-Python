'''
Faca um programa que tenha uma funcao chamada 
maior, que receba 
varios parametros com valores inteiros.
Seu programa tem que analisar todos os valores e 
dizer qual deles e maior
'''


def maior(*valor):
    maior = max(valor)
    tam = len(valor)
    print('=-=' * 8)
    print(f'Valores: {valor}')
    print(f'{tam} valores informados')
    print(f'O maior valor foi {maior}')
    print('=-=' * 8)


maior(2, 3, 7, 1)
maior(2, 9, 4, 5, 7, 1)
maior(1, 2)
maior(6)
