n = int(input('Informe o valor: '))
print('A tabuada é')
print('-' * 11)
for i in range(0, 11):
    print('{} * {} = {}\n'.format(n, i, n * i))
print('-' * 11)

a = 1

# tabuada completa
while a <= 10:
    b = 1
    while b <= 10:
        print('{} * {} = {}'.format(a, b, a * b))
        b += 1
    a += 1
    print('\n')
