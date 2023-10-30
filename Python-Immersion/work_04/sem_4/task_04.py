'''
Задание №4

✔ Функция получает на вход список чисел.
✔ Отсортируйте его элементы in place без использования
встроенных в язык сортировок.
✔ Как вариант напишите сортировку пузырьком.
Её описание есть в википедии.
'''

from random import randint
from timeit import timeit


orig_list = [randint(-100, 100) for _ in range(10)]


def buble_sort(lst):
    n = 1
    while n < len(lst):
        for i in range(len(lst) - n):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
        n += 1
 
    return lst

print(buble_sort(orig_list[:]))
print(orig_list)

print(timeit('buble_sort(orig_list[:])', globals=globals(), number=100))
