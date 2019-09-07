try:
    a = int(input('Primeiro número: '))
    b = int(input('egundo número: '))
    r = a / b
except Exception as erro:
    print(f'ERR: {erro.args[0]}')
else:
    print(f'O resultado é {r:.1f}')
finally:
    print('Divisão finalizada')