"""
Реализовать функцию int_func(), принимающую слово из маленьких латинских
букв и возвращающую его же, но с прописной первой буквой.
Например, print(int_func("text")) -> Text.
Продолжить работу над заданием. В программу должна попадать строка из слов,
разделенных пробелом. Каждое слово состоит из латинских букв в нижнем регистре.
 Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной
  буквы. Необходимо использовать написанную ранее функцию int_func().
"""

from timeit import timeit


def int_func(word):

    """
    Использование стандартного метода title()
    :param word: строка
    :return: Строка со словами, начинающимися с заглавныъ букв
    """
    return word.title()


def my_func(word):
    """
    Аналог метода title()
    :param word: строка
    :return: Возвращает слово с первой заглавной буквой
    """
    mylist = list(word)  # преобразуем строчку в список
    mylist[0] = mylist[0].upper()  # меняем регистр 0-элемента
    return print(''.join(mylist), end=' ')  # преобразем строчку в список


with open('file.txt', 'r', encoding="utf-8") as data:
    line = data.readlines()
    for text in line:
        text.split()


print(timeit("""
string = text.split()
for el in string:
    my_func(el)
""", globals=globals(), number=1000))


print(f'\n{int_func(text)}')
print(timeit("int_func(text)", globals=globals(), number=1000))


"""
Произвел замеры времени:

1) Первый метод - перебор строки по слову, в котором первая буква меняется на 
заглавную.
Потраченное время: 0.4612069000140764

2) Второй метод - использование стандартного метода title()
Потраченноое время: 0.006474299996625632

Вывод: использование метода title() ускорило работу программы в 71 раз
"""