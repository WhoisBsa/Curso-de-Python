"""
Refaça o desafio 035 dos triângulos, acrescentando o recurso de mostar que tipo de
triângulo será formado:
- Equilátero: todos os lados iguais
- Isóceles: dois lados iguais
- Escaleno: todos os lados diferentes
"""
r1 = int(input('Valor da reta 1: '))
r2 = int(input('Valor da reta 2: '))
r3 = int(input('Valor da reta 3: '))

if (r1 + r2) > r3 and (r2 + r3) > r1 and (r1 + r3) > r2:
    if r1 == r2 == r3:
        print('Triângulo Equilátero')
    elif r1 == r2 or r2 == r3 or r1 == r3:
        print('Triângulo Isóseles')
    else:
        print('Triângulo Escaleno')
else:
    print('Não é possível formar um triângulo')