"""
Faça um programa que leia um nome de usuário e sa sua senha e nçao aceite a senha
igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.
"""
'''
        nome = str(input('Digite seu nome: '))
        senha = str(input('Digite sua senha: '))
        
        while nome == senha:
                print('O nome de usuário e senha se coincidem, por favor informe um valor diferente.')
                nome = str(input('Digite seu nome: '))
                senha = str(input('Digite sua senha: '))
        print('Usuário casdastrado com sucesso!')
'''

"""
Faça um programa que gera uma lista dos números primos existentes entre 1 e um número
inteiro informado pelo usuário.
"""

n = int(input('Digite um número: '))
cont = 0
c = 0

for i in range(1, n):
        cont += 1
        if n % i == 0:
                c += 1
        if c < 2:
                print('{}'.format(i), end=' ')
