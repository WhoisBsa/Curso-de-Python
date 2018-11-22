for c in range(0, 6):
    print('Oi')
print('Fim')

for c in range(6, 0, -1):
    print(c)
print('Fim')

for c in range(0, 6, 2):
    print(c)
print('Fim')

n = int(input('Digite um numero: '))
for c in range(0, n+1):
    print(c)
print('Fim')

i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo '))

for c in range(i, f+1, p):
    print(c)
print('Fim')

for c in range(0, 3):
    p = int(input('Digite um valor: '))
print('Fim')

s = 0
for c in range(0, 4):
    p = int(input('Digite um valor: '))
    s += n
print('O somatório de todos os valores foi {}'.format(s))
