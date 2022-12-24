"""
Реализовать генератор с помощью функции с ключевым словом yield, создающим
очередное значение.

При вызове функции должен создаваться объект-генератор.

Функция должна вызываться следующим образом: for el in fact(n).

Функция отвечает за получение факториала числа, а в цикле необходимо выводить
только первые n чисел, начиная с 1! и до n!.

Подсказка: факториал числа n — произведение чисел от 1 до n.

Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.
"""


def factorial(num):
    """
    Нахождение факториала числа
    :param num: число
    :return: значение факториала
    """
    if num == 1:
        return 1
    else:
        return num * factorial(num-1)


n = int(input('Введите число: '))


def fact(n):
    """
    Фуекция-генератор факториала числа
    :param n: число
    :return: генератор факториалов
    """
    for i in range(1, n+1):
        print(i, end='! = ')
        yield factorial(i)


for el in fact(n):
    print(el)