n = [0] * 3
maior = n[0]
menor = n[0]
for i in range(0, 3):
    n[i] = int(input('Digite um numero: '))
    if i == 0:
        maior = n[0]
        menor = n[0]
    else:
        if n[i] >= maior:
            maior = n[i]

        if n[i] <= menor:
            menor = n[i]

print('Maior: ', maior)
print('Menor: ', menor)
