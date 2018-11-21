"""
Desenvolva um lógica que leia o peso e a altura de uma pessoa, calcule seu IMC
e mostre seu status, de acordo com a tabela abaixo:
- Abaixo de 18.5: Abaixo do peso
- Entre 18.5 e 25: Peso ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade mórbida
"""

peso = float(input('Peso: '))
h = float(input('Altura: '))
imc = peso / (h ** 2)
print(f'Seu imc é {imc:.2f} e você está ', end='')

if imc < 18.5:
    print('abaixo do peso')
elif imc >= 18.5 and imc <= 25:
    print('no peso ideal')
elif imc >25 and imc <= 30:
    print('no sobrepeso')
elif imc > 30 and imc <= 40:
    print('obeso')
else:
    print('na obesidade mórbida')