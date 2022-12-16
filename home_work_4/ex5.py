"""
Реализовать формирование списка, используя функцию range() и возможности
генератора.
В список должны войти четные числа от 100 до 1000 (включая границы). 
Необходимо получить результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce().
"""
from functools import reduce

mylist = [el for el in range(100, 1001) if el % 2 == 0]

res = reduce(lambda x, y: x * y, mylist)
print(res)


def my_func(prev_el, el):
    """
    Умножение элементов
    :param prev_el: предыдущий элемент
    :param el: текущий элемент
    :return: произведение элементов
    """
    return prev_el * el


print(reduce(my_func, mylist))



# mult = 1
# for el in mylist:
#     mult *= el
# print(mult)
