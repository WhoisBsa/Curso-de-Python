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


def contador(*num):
	tam = len(num)
print(f'Recebi os valores {num} e sao ao todo {tam} numeros')


contador(2, 4, 5, 8)
contador(1, 9, 3)
contador(3, 2)


def dobra(lst):
	pos = 0
	while pos < len(lst):
		lst[pos] *= 2
		pos += 1


valores = [6, 7, 2, 5, 4, 0, 1]
dobra(valores)
print(valores)


def soma(*valores):
	s = 0
	for num in valores:
		s += num
	print(f'Somando os valores {valores} temos {s}')


soma(5, 2)
soma(2, 9, 4)
