from timeit import timeit
from memory_profiler import profile


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

n1, n2, n3 = int(input("Введите число: ")), int(input("Введите число: ")), int(input("Введите число: "))
print(f'{sum_max_elements(n1, n2, n3)}')

print(timeit("sum_max_elements(n1, n2, n3)", globals=globals(), number=1000))


def sum_two_elements(lst):
    mylist = [int(x) for x in lst]
    return sum(mylist) - min(mylist)


num = input("Введите три числа через пробел: ").split()
print(sum_two_elements(num))

print(timeit("sum_two_elements(num)", globals=globals(), number=1000))
