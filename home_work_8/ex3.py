"""
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на н0ль.
Проверьте его работу на данных, вводимых пользователем.
При вводе пользователем нуля в качестве делителя,
программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


class ZeroDivision(Exception):

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2


def divizion():
    try:
        a, b = int(input('Введите число:\t')), int(input('Введите число:\t'))
        if b == 0:
            raise ZeroDivision(a, b)
    except ValueError:
        print('Вы ввели не число')
    except ZeroDivision:
        print('Деление на ноль')
    else:
        print(a / b)


divizion()
