"""
Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo
um sistema de visualização de detalhes do aproveitamento de cada jogador.
"""


jogadores = list()
jogador = dict()

while True:
    jogador['nome'] = str(input('Nome do jogador: '))
    partidas = int(input('Quantidade de partidas: '))
    gols = [] * partidas

    for i in range(0, partidas):
        gols.append(int(input(f'{" ":>5}Gols na {i+1}º partida: ')))

    jogador['gols'] = gols
    jogador['total'] = sum(gols)

    jogadores.append(jogador.copy())

    op = str(input('Quer continuar? [S/N] ')).upper().strip()
    while op not in 'SN':
        print('Apenas S/N, tente novamente. ')
        op = str(input('Quer continuar? \033[31m[S/N]\033[m ')).upper().strip()
    if op in 'N':
        print('=-=' * 13)
        break

# printar a tabela de jogadores
print(f'cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 40)
for k, v in enumerate(jogadores):
    print(f' {k:<3}', end='')
    for dado in v.values():
        print(f'{str(dado):<15} ', end='')
    print()
print('-' * 40)

# detalhes do aproveitamento de cada jogador
while True:
    levantamento = int(input('Mostrar dados de qual jogador? (-1 para sair) '))
    while levantamento > len(jogadores)-1:
        levantamento = int(input('Valor inválido, tente novamente: (-1 para sair) '))
    if levantamento == -1:
        print('=-=' * 16)
        print('<<<' * 2, 'Fim do programa', '>>>' * 2)
        break

    for i, j in enumerate(jogadores):
        if i == levantamento:
            print(f'{">>":>5} Levantamento do jogador {j["nome"]}')
            for k, v in enumerate(j['gols']):
                print(f'{" ":>5} No jogo {k+1}, {j["nome"]} fez {v} gols')
    print('-' * 49)
