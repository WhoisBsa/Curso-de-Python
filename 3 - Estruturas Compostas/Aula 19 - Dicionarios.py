pessoas = {'nome': 'matheus', 'sexo': 'M', 'idade': 19}

print(pessoas)
print(pessoas['nome'])
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
print(pessoas.items())

for k, v in pessoas.items():
    print(f'{k} = {v}')

del pessoas['sexo']

pessoas['nome'] = 'João'
pessoas['peso'] = 77.5
print(pessoas)

brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil)
print(brasil[0])
print(brasil[0]['uf'])

estado = dict()
brazil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brazil.append(estado.copy())
for e in brazil:
    for k, v in e.items():
        print(f'{k}: {v}')
    print()
