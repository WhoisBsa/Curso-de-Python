nome = str(input('Nome: '))
separa = nome.split()
if separa[0] == 'Matheus':
    print('lindo')
print('Bom dia, {}'.format(separa[0]))

n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))
m = (n1 + n2)/2
print('Sua media foi boa' if m >= 6 else 'Sua media foi ruim')