def double(n=0, coin=False):
    if coin:
        return moeda(n * 2)
    return n * 2


def half(n=0, coin=False):
    if coin:
        return moeda(n / 2)
    return n / 2


def plus(n=0, t=0, coin=False):
    if coin:
        return moeda(n + (n * (t / 100)))
    return n + (n * (t / 100))


def decrease(n=0, t=0, coin=False):
    if coin:
        return moeda(n - (n * (t / 100)))
    return n - (n * (t / 100))


def moeda(n=0):
    return f'R${n:.2f}'.replace('.', ',')
