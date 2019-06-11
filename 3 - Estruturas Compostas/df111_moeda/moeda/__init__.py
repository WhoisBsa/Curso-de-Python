def double(n=0, coin=False):
    if coin:
        return moeda(n * 2)
    return n * 2


def half(n=0, coin=False):
    if coin:
        return moeda(n / 2)
    return n / 2


def plus(n=0, p=0, coin=False):
    if coin:
        return moeda(n + (n * (p / 100)))
    return n + (n * (p / 100))


def decrease(n=0, d=0, coin=False):
    if coin:
        return moeda(n - (n * (d / 100)))
    return n - (n * (d / 100))


def moeda(n=0):
    return f'R${n:.2f}'.replace('.', ',')


def resumo(n, p, d):
    print(f'{"-"*29} \n{"RESUMO DO VALOR".center(29)}\n{"-"*29}')
    print(f'Preço analizado: \t{moeda(n)} ')
    print(f'Dobro do preço: \t{double(n, True)}')
    print(f'Metade do preço: \t{half(n, True)}')
    print(f'{p}% de aumento: \t{plus(n, p, True)}')
    print(f'{d}% de desconto: \t{decrease(n, d, True)}')
