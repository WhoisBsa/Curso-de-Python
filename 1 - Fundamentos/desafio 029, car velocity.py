carro = float(input('Velocidade do carro: '))

if carro <= 80:
    print('Passou de boa')
else:
    print('Teu carro foi multado em {:.1f}R$'.format((carro - 80)*7))