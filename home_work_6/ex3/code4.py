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
    :return: Строка со словами, начинающимися с заглавныъ букв
    """
    return word.title()


print(f'\n{int_func(text)}')