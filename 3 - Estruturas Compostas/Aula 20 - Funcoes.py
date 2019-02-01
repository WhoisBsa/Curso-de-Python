def mostralinha():
    print('-' * 30)


mostralinha()
print('matheus')
mostralinha()
print('barbosa')
mostralinha()
print('souza')
mostralinha()

print()

nome = {1: 'matheus', 2: 'barbosa', 3: 'souza'}

def mensagem(msg):
    print('-' * 30)
    print(msg)
    print('-' * 30)


def main():
    for i in range(1, 4):
        msg = nome[i]
        mensagem(msg)

if __name__ == '__main__':
    main()