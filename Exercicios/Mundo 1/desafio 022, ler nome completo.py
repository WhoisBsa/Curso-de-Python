nome = str(input('Digite seu nome completo: '))

lMaiusculas = nome.split()
print(lMaiusculas[0].upper())
print(lMaiusculas[0].lower())
print(len(nome)-nome.count(' '))
print(len(lMaiusculas[1]))