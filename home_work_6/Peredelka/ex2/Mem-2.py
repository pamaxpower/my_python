import random
from memory_profiler import profile

my_list = [random.randint(-1000, 1000) for _ in range(10000)]

@profile
def var_1(lst):
    new_list = []
    for j in range(1, len(lst) - 1):
        if lst[j] > lst[j - 1]:
            new_list.append(lst[j])
    return new_list


var_1(my_list)
#print(f'Первый способ: {var_1(mylist)}')

"""
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
     6     26.3 MiB     26.3 MiB           1   @profile
     7                                         def var_1(lst):
     8     26.3 MiB      0.0 MiB           1       new_list = []
     9     26.3 MiB      0.0 MiB        9999       for j in range(1, len(lst) - 1):
    10     26.3 MiB      0.0 MiB        9998           if lst[j] > lst[j - 1]:
    11     26.3 MiB      0.0 MiB        5019               new_list.append(lst[j])
    12     26.3 MiB      0.0 MiB           1       return new_list
"""


@profile
def var_2(lst):
    res_list = [lst[j] for j in range(1, len(lst) - 1) if
                lst[j] > lst[j - 1]]
    return res_list


var_2(my_list)
# print(f'Второй способ: {var_2()}')

"""
    31     26.3 MiB     26.3 MiB           1   @profile
    32                                         def var_2(lst):
    33     26.4 MiB      0.0 MiB       15020       res_list = [lst[j] for j in range(1, len(lst) - 1) if
    34     26.4 MiB      0.0 MiB       15018                   lst[j] > lst[j - 1]]
    35     26.4 MiB      0.0 MiB           1       return res_list
"""

"""
Произвел замеры памяти:

1) Первый способ: результирующий список создается путем перебора элементов исходного списка и 
добавление элементов, подходящих условию, в новый список.
Размер потраченной памяти: 26,3 MiB

2) Второй способ: получение результирующего 
списка с помощью LC
Размер потраченной памяти: 26,3 MiB

Вывод: оба способа расходуют одинаковое количество памяти
"""
