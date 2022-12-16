'''
Проверить гипотезу о быстром поэлементном объединении двух отсортированных массивов.

На входе подается два рандромно заполненных и отсортированных масиива

На выходе должен получиться один отсортированный массив
'''

from timeit import timeit
import random


def quick_merge(list1, list2):
    """
    Функция принимает на вход два отсортированных массива и поэлементно их объединяет.
    :param list1:
    :param list2:
    :return: 
    """
    result = []
    p1 = 0          # создаем численные указатели для начала списков
    p2 = 0  
    while p1 < len(list1) and p2 < len(list2):  # проверка не закончился ли список
        if list1[p1] <= list2[p2]: # ищем меньший элемент
            result.append(list1[p1]) # и добавляем его в новый список
            p1 += 1 # увеличиваем указатель на первый элемент
        else:
            result.append(list2[p2])
            p2 += 1
    if p1 < len(list1): # когда один из список закончился, 
        result += list1[p1:] # добавляем оставшиеся элементы другого списка
    if p2 < len(list2):
        result += list2[p2:]    
    return result


def merge(list1, list2):
    return sorted(list1 + list2)


def new_merge(list1, list2):
    res = list1 + list2
    res.sort()
    return res


numbers1 = sorted([random.randint(1, 2000000) for _ in range(1000000)])
numbers2 = sorted([random.randint(1, 2000000) for _ in range(2000000)])

quick_merge(numbers1, numbers2)
print(f'Время выполнения quick_merge: {timeit("quick_merge(numbers1, numbers2)", globals=globals(), number=100)}')
# 153.48526719998335


merge(numbers1, numbers2)
print(f'Время выполнения merge: {timeit("merge(numbers1, numbers2)", globals=globals(), number=100)}')
# 52.15125719999196

new_merge(numbers1, numbers2)
print(f'Время выполнения new_merge: {timeit("new_merge(numbers1, numbers2)", globals=globals(), number=100)}')
# 40.89479419999407

# Функция быстрого слияния двух отсортированных списков работает значительно медленнее, 
# чем стандартные функции sort() и sorted()
# Функция list.sort() примерно на 20% быстрее, чем sorted()