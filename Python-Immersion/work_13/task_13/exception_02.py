def get(text: str = None) -> int:
    data = input(text)
    num = int(data)
    return num


if __name__ == '__main__':
    number = get('Введите целый делитель: ')
    print(f'100 / {number} = {100 / number}')

# возникнет ошибка, которая находится в 3 строке кода 
# (нельзя привести "сорок два" к целочисленному значению),
# но эта ошибка сама не могла возникнуть. 
# Она была вызвана 8 строкой кода
# таким образом мы видим весь путь происхождения ошибки