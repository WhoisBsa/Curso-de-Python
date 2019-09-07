"""
Reescreva a função leiaint() incluindo agora a possibilidade
da digitação de um número de tipo inválido. Aproveite e crie
uma função leiafloat() com a mesma funcionalidade.
"""


def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except KeyboardInterrupt:
            print(f'\033[31;3mO usuário preferiu não informar o número. \033[m')
            n = 0
            result = f'O número inteiro digitado foi {n}'
            break
        else:
            result = f'O número inteiro digitado foi {n}'
            break
    return result

def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print(f'\033[31;3mTipo de dado errado, digite apenas números inteiros. \033[m')
        except KeyboardInterrupt:
            print(f'\033[31;3mO usuário preferiu não informar o número. \033[m')
            n = 0
            result = f'O número real digitado foi {n}'
            break
        else:
            result = f'O número real digitado foi {n}'
            break
    return result

i = leiaInt('Digite um número inteiro: ')
f = leiaFloat('Digite um número real: ')
print(i)
print(f)
