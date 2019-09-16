
op = 0
while op != 3:
    with open('cadastros.txt', 'a') as file:
        print('-'*40)
        print('Cadastro de Clientes'.center(40))
        print('-'*40)
        print('MENU')
        print("""1 - Vizualizar\n2 - Cadastrar\n3 - Sair""")
        try:
            op = int(input("Selecione uma opção: "))
        except (ValueError, TypeError):
            print(f'\033[33;31mErro: digite apenas numeros inteiros válidos.\033[m')
        print('-'*40)

        if op == 1:
            file = open('cadastros.txt', 'r')
            for line in file.readlines():
                print(line)
            file.close()
        if op == 2:
            nome = str(input('Nome: ')).strip().capitalize()
            try:
                idade = int(input('Idade: '))
            except (ValueError, TypeError):
                print(f'\033[33;31mErro: digite apenas numeros inteiros válidos.\033[m')
            file.write(f'{nome:<28}{idade:>7} anos\n')
        if op == 3:
            print('Volte sempre'.center(40))
            print('-'*40)

