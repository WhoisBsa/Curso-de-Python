r1 = int(input('Valor da reta 1: '))
r2 = int(input('Valor da reta 2: '))
r3 = int(input('Valor da reta 3: '))

if (r1 + r2) > r3 and (r2 + r3) > r1 and (r1 + r3) > r2:
    print('{}, {} e {} podem formar um triangulo'.format(r1, r2, r3))
else:
    print('{}, {} e {} nao podem formar um triangulo'.format(r1, r2, r3))
