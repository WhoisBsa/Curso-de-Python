frase = str(input('Frase: ')).upper().strip()
print('Tem {} As'.format(frase.count('A')))
print('Primeiro A na posição {}'.format(frase.find('A')+1))
print('Ultimo A na posição {}'.format(frase.rfind('A')+1))