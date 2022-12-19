# 1. Создать класс-исключение от класса Exception
# 2. Сгенерировать исключение в нужной точке программы
# 3. Отловить и обработать

from sys import exit


class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt
        #exit(1)


inp_data = input("Введите положительное число: ")

try:
    inp_data = int(inp_data)
    if inp_data < 0:
        raise OwnError("Вы ввели отрицательное число!")
except ValueError:
    print("Вы ввели не число")
except OwnError as err:
    print(err)
else:
    print(f"Все хорошо. Ваше число: {inp_data}")



"""
Введите положительное число: 5
Все хорошо. Ваше число: 5

Введите положительное число: text
Вы ввели не число

Введите положительное число: -65
Вы ввели отрицательное число!
"""
