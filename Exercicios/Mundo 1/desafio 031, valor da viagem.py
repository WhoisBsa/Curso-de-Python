viagem = float(input('Distancia da viagem: '))

if viagem <= 200:
    print('A passagem custa {}R$'.format(viagem*0.5))
else:
    print('A passagem custa {}R$'.format(viagem*0.45))
