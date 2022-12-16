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

quick_merge(numbers1, numbers2)


@profile
def merge(list1, list2):
    return sorted(list1 + list2)

merge(numbers1, numbers2)

@profile
def new_merge(list1, list2):
    res = list1 + list2
    res.sort()
    return res

new_merge(numbers1, numbers2)