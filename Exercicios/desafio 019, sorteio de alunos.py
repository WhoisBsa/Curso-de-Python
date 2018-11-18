from random import choice
aluno = [0]*4
for i in range(0, 4):
    aluno[i] = str(input('Nome do {}º aluno: '.format(i+1)))
escolhido = choice(aluno)
print('Aluno escolhido foi: {}'.format(escolhido))