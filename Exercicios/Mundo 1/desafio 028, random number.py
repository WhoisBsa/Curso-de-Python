import random

n = random.randrange(0, 6)

for i in range(0,3):
    chance = int(input('Escolha: '))
    if chance == n:
        print('Uhul, ganhou')
        break
    else:
        print('Loser')