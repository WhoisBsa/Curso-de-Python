"""
Faca um programaque tenha uma funcao notas() que pode receber varias notas de alunos
e vai retornar um dicionario com as seguintes informacoes:
Quantidade de notas
A maior nota
A media da turma
A situacao (opcional)
"""


def notas(*n, sit=False):
    aluno = {}
    aluno['total'] = len(n)
    aluno['maior'] = max(n)
    aluno['media'] = round(sum(n) / float(len(n)), 2)
    
    #valida a situacao do aluno
    if sit:
    	if aluno['media'] < 6:
    	    aluno['situacao'] = 'RUIM'
    	elif 6 <= aluno['media'] < 7:
    	    aluno['situacao'] = 'Razoavel'
    	else:
    	    aluno['situacao'] = 'BOA'
    
    return aluno

resp = notas(6, 8.5, 7.75, 6.25, sit=True)
for k, v in resp.items():
    print(f'{k}: {v}')
