num = [2, 5, 9, 1]
num[2] = 3
print(num)

num.append(7)
print(num)

num.sort()
print(num)

num.sort(reverse=True)
print(num)

num.insert(2, 0)
print(num)

num.pop()
print(num)

num.pop(2)
print(num)

num.insert(2, 2)
print(num)

num.remove(2)
print(num)

if 5 in num:
    num.remove(5)
print('Não achei o numero 5')


valores = []
valores.append(5)
valores.append(9)
valores.append(4)

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}')
print('Cheguei ao final da lista')


val = list()
for cont in range(0, 5):
    val.append(int(input('Digite um valor: ')))
print(val)


a = [2, 3, 4, 7]
# b = a ligação, por isso se alterar uma altera a outra
b = a[:] # quando há uma cópia esse problema é resolvido
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista A: {b}')
