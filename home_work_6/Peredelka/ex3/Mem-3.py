from memory_profiler import profile
import random

numbers1 = sorted([random.randint(1, 10000) for _ in range(100)])
numbers2 = sorted([random.randint(1, 10000) for _ in range(200)])


@profile
def quick_merge(list1, list2):
    """
    Функция принимает на вход два отсортированных массива и поэлементно их объединяет.
    :param list1:
    :param list2:
    :return: 
    """
    result = []
    p1 = 0  # создаем численные указатели для начала списков
    p2 = 0
    while p1 < len(list1) and p2 < len(
            list2):  # проверка не закончился ли список
        if list1[p1] <= list2[p2]:  # ищем меньший элемент
            result.append(list1[p1])  # и добавляем его в новый список
            p1 += 1  # увеличиваем указатель на первый элемент
        else:
            result.append(list2[p2])
            p2 += 1
    if p1 < len(list1):  # когда один из список закончился,
        result += list1[p1:]  # добавляем оставшиеся элементы другого списка
    if p2 < len(list2):
        result += list2[p2:]
    return result


quick_merge(numbers1, numbers2)

"""
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
     9     26.1 MiB     26.1 MiB           1   @profile
    10                                         def quick_merge(list1, list2):
    17     26.1 MiB      0.0 MiB           1       result = []
    18     26.1 MiB      0.0 MiB           1       p1 = 0          # создаем численные указатели для начала списков
    19     26.1 MiB      0.0 MiB           1       p2 = 0
    20     26.1 MiB      0.0 MiB         299       while p1 < len(list1) and p2 < len(list2):  # проверка не закончился ли список
    21     26.1 MiB      0.0 MiB         298           if list1[p1] <= list2[p2]: # ищем меньший элемент
    22     26.1 MiB      0.0 MiB         100               result.append(list1[p1]) # и добавляем его в новый список
    23     26.1 MiB      0.0 MiB         100               p1 += 1 # увеличиваем указатель на первый элемент
    24                                                 else:
    25     26.1 MiB      0.0 MiB         198               result.append(list2[p2])
    26     26.1 MiB      0.0 MiB         198               p2 += 1
    27     26.1 MiB      0.0 MiB           1       if p1 < len(list1): # когда один из список закончился,
    28                                                 result += list1[p1:] # добавляем оставшиеся элементы другого списка
    29     26.1 MiB      0.0 MiB           1       if p2 < len(list2):
    30     26.1 MiB      0.0 MiB           1           result += list2[p2:]
    31     26.1 MiB      0.0 MiB           1       return result

"""


@profile
def merge(list1, list2):
    return sorted(list1 + list2)


merge(numbers1, numbers2)

"""
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    36     26.2 MiB     26.2 MiB           1   @profile
    37                                         def merge(list1, list2):
    38     26.2 MiB      0.0 MiB           1       return sorted(list1 + list2)
"""


@profile
def new_merge(list1, list2):
    res = list1 + list2
    res.sort()
    return res


new_merge(numbers1, numbers2)

"""
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    42     26.2 MiB     26.2 MiB           1   @profile
    43                                         def new_merge(list1, list2):
    44     26.2 MiB      0.0 MiB           1       res = list1 + list2
    45     26.2 MiB      0.0 MiB           1       res.sort()
    46     26.2 MiB      0.0 MiB           1       return res
"""

# Вывод: во всех трех способах разницы в используемой памяти нет
