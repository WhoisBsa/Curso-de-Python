def double(n=0):
    return n * 2


def half(n=0):
    return n / 2


def plus(n=0, t=0):
    return n + (n * (t / 100))


def decrease(n=0, t=0):
    return n - (n * (t / 100))


def moeda(n=0):
    return f'R${n:.2f}'.replace('.', ',')
