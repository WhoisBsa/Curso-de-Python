#################################################################
#   Crie um programa onde o usuário possa digitar sete valores  #
#   numéricos e cadastre-os em uma lista única que mantenha     #
#   separadosos valores pares e ímpares. No final, mostre os    #
#   valores pares e ímpares em ordem crescente.                 #
#################################################################

numeros = [[], []]
valor = 0
for i in range(0, 7):
    valor = int(input(f'Digite o {i+1}º número:'))
    if valor % 2 == 0:
        numeros[0].append(valor)
    else:
        numeros[1].append(valor)
numeros[0].sort()
numeros[1].sort()
print('=-=' * 4)
print(f'Todos os valores pares {numeros[0]}')
print(f'Todos os valores ímpares {numeros[1]}')
