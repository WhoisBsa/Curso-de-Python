def read_money(price):
    while True:
        value = str(input(price)).replace(',', '.').strip()
        if value.isalpha() or value == '':
            print(f'\033[0;31mERRO \"{value}\" é um valor inválido\033[m')
        else:
            return float(value)
            break
