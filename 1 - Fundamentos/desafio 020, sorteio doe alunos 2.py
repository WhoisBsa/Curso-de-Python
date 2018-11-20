import random
aluno = [0]*4
for i in range(0, 4):
    aluno[i] = str(input('Nome do {}º aluno: '.format(i+1)))
escolhido = random.sample(aluno, len(aluno))
print('A ordem dos alunos escolhidos sao: {}'.format(escolhido))
