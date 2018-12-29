"""
Crie um programa onde o usuário digite uma expressão qualquer que use
parêntese. Seu aplicativo deverá analisar se a expressão passada está
com os parênteses abertos e fechados na ordem correta.
"""

expressao = list()
exp = str(input('Digite a expressão: '))
for simb in exp:
    if simb == '(':
        expressao.append('(')
    elif simb == ')':
        if len(expressao) > 0:
            expressao.pop()
        else:
            expressao.append(')')
            break
if len(expressao) == 0:
    print('Sua expressão é válida')
else:
    print('Sua expressão não é válida')