nome = str(input('Qual é seu nome? '))
if nome == 'Matheus':
    print('Que nome bonito!')
elif nome == 'João' or nome == 'Maria' or nome == 'José':
    print('Seu nome é bem popular no Brasil.')
else:
    print('Seu nome é normal.')
print('Tenha um bom dia, {}'.format(nome))
