n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))

s = n1 + n2
d = n1 / n2
m = n1 * n2
di = n1 // n2
e = n1 ** n2

print('A soma vale {},\nA divisao vale {:.2f},\nA mutiplicaçao vale,\n'.format(s, d, m), end='')
print('A divisao inteira vale {},\nA a potencia vale {}.'.format(di, e))