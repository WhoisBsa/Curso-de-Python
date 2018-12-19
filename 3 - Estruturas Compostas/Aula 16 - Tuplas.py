lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
print(lanche[-1])

lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
print(lanche[1:3])

lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
print(lanche)

lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
for c in lanche:
	print(f'Eu vou comer {c}')
print('Comi pra caramba!')

for c in range(0, len(lanche)):
	print(f'Eu vou comer {lanche[c]}')
print('Comi pra caramba!')

for pos, c in enumerate(lanche):
	print(f'Eu vou comer {c} na posicao {pos}')
print('Comi pra caramba!')

print(sorted(lanche))

print('\n')

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a
print(c)
print(c.count(5))  # conta quantas vezes o elemento aparece
print(c.index(8))  # mostra em qual posiçao o elemento se encontra

pessoa = ('Matheus', 18, 'M', 74.05)
print(pessoa)
