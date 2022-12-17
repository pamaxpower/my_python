from memory_profiler import profile

with open('file.txt', 'r', encoding="utf-8") as data:
    line = data.readlines()
    for text in line:
        text.split()

@profile
def my_func(word):
    """
    Аналог метода title()
    :param word: строка
    :return: Возвращает слово с первой заглавной буквой
    """
    mylist = list(word)  # преобразуем строчку в список
    mylist[0] = mylist[0].upper()  # меняем регистр 0-элемента
    return print(''.join(mylist), end=' ')  # преобразем строчку в список


string = text.split()
for el in string:
    my_func(el)


@profile
def int_func(word):

    """
    Использование стандартного метода title()
    :param word: строка
    :return: Строка со словами, начинающимися с заглавных букв
    """
    return word.title()


print(f'\n{int_func(text)}')

"""
Произвел замеры памяти:

1) Первая функция - написанный мною аналог метода title(), 
который берет каждое слово из строчки и возвращает его с заглавной буквой. 
Размер потраченной памяти: 25,6 MiB

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
     8     25.6 MiB     25.6 MiB           1   @profile
     9                                         def my_func(word):
    15     25.6 MiB      0.0 MiB           1       mylist = list(word)  # преобразуем строчку в список
    16     25.6 MiB      0.0 MiB           1       mylist[0] = mylist[0].upper()  # меняем регистр 0-элемента
    17     25.6 MiB      0.0 MiB           1       return print(''.join(mylist), end=' ')  # преобразем строчку в список

2) Вторая функция - использование стандартного метода title()/
Размер потраченной памяти: 25,7 MiB
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    25     25.7 MiB     25.7 MiB           1   @profile
    26                                         def int_func(word):
    33     25.7 MiB      0.0 MiB           1       return word.title()


Вывод: количество, требуемой памяти для обеих функций существенно не отличается
"""