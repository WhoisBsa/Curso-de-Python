'''for c in range(1, 10):
    print(c)
print('Fim')'''

'''c = 1
while c < 10:
    print(c)
    c +=1
print('Fim')'''

'''for c in range(1, 10):
    n = int(input('Valor: '))
print('Fim')'''

'''n = 1
while n != 0:
    n = int(input('Valor: '))
print('Fim')'''

n = 1
par = impar = 0
while n != 0:
    n = int(input('Valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('Voce digitou {} numeros pares e {} numeros impares'.format(par,impar))
