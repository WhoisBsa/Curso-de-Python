teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(teste)
print(galera)


pessoas = [['Joao', 19], ['Ana', 33], ['Maria', 45]]
print(pessoas[::-1])
for p in pessoas:
    print(f'{p[0]} tem {p[1]} anos de idade.')

gente = list()
dado = list()
totmai = totmen = 0
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    gente.append(dado[:])
    dado.clear()
print(gente)
for p in gente:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmen += 1
print(f'Temos {totmai} maiores e {totmen} menores de idade.')