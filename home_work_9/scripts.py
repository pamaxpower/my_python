"""
Примеры из домашних работа
"""


# ДЗ-3 зад 4 - На равенство
def my_func(num, neg):
    """
    Функция вовзведения числа в степень через произведение
    :param num: Любое положительное действительное число
    :param neg: Любое целое отрицательное число
    :return: числа num в степени neg
    """
    mult = num ** neg
    return mult


# ДЗ-4 зад 4 - на равенство и bool True 
def unique_items(lst):
    res_list = [el for el in lst if lst.count(el) == 1]
    return res_list


# ДЗ-4 зад 2 - на равенство и bool False
def larger_item(lst):
    return [lst[j] for j in range(1, len(lst)-1) if lst[j] > lst[j-1]]


# ДЗ-7 зад 4 - на принадлежность классу
class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police


# ДЗ-8 зад 2 - на ссылку на 1 объект, не равно, ошибка деления на 0,
class Cell:
    def __init__(self, quantity):
        self.quantity = int(quantity)

    def __str__(self):
        return str(self.quantity)

    def __sub__(self, other):
        if self.quantity < other.quantity:
            return f'Неверный результат. Разность количества ячеек меньше ' \
                   f'нуля\n '
        else:
            return f'Выполняем вычитание: ' \
                   f'{Cell(self.quantity - other.quantity)}\n'

    def __truediv__(self, other):
        return f'Выполняем деление: {Cell(self.quantity / other.quantity)}\n'


# ДЗ-8 зад 3 - на ошибки
class ZeroDivision(Exception):

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2


def divizion(a, b):
    if b == 0:
        raise ZeroDivision(a, b)
    return a / b
