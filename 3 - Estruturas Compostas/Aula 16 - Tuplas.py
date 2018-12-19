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
