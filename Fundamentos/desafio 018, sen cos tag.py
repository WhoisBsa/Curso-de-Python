import math
angulo = float(input('Angulo de: '))
sen = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tag = math.tan(math.radians(angulo))
print(f'O ângulo {angulo} tem os valores de \nseno: {sen:.2f} \ncoseno: {cos:.2f} \ntangente: {tag:.2f}')