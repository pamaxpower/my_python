"""
Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
"""


def sum_max_elements(a, b, c):
    """
    "Функция, выполняющая сложение двух максимальных элементов"
    :param a: Любое целое число
    :param b: Любое целое число
    :param c: Любое целое число
    :return: Сумма элементов
    """
    small = a
    if b < a or c < a:
        small = b
        if c < b:
            small = c

    total = a + b + c - small
    return total


def sum_elements(a, b, c):
    total = a + b + c - min(a, b, c)
    return total


n1, n2, n3 = int(input()), int(input()), int(input())
print(f'Первый спсособ: {sum_elements(n1, n2, n3)}')
print(f'Второй способ: {sum_max_elements(n1, n2, n3)}')
