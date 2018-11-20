import math
caOp = float(input('Cateto oposto: '))
caAd = float(input('Cateto adjacente: '))
print(f"A hipotenusa é: {math.hypot(caOp, caAd):.2f}")