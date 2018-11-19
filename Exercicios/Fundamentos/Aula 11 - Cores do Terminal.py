#print('\033[7;30mOlá, Mundo!!\033[m')

a = 3
b = 5

#print("Os valores são \033[32m{}\033[m e \033[31m{}\033[m".format(a, b))

nome = 'Matheus'
cores = {'limpa': '\033[m', 'azul': '\033[34m', 'pretoebranco': '\033[7;30m'}
print('Hy! Nice to meet you, {}{}{}!!!'.format(cores['pretoebranco'], nome, cores['limpa']))