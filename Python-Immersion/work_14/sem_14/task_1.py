'''
Задание №1

Создайте функцию, которая удаляет из текста все символы
кроме букв латинского алфавита и пробелов.
Возвращается строка в нижнем регистре.
'''
import re


def func(text):
    result = ''
    for el in text:
        if el.isalpha() and 'a' <= el.lower() <= 'z' or el.isspace():
            result += el.lower()
    return result


def convert_str(text):
    '''Удаляет из текста все символы, кроме
    букв латинского алфавита и пробелов '''
    # убираем все кроме букв a-z, A-Z и пробела
    new_str = re.compile('[^a-zA-Z ]')
    res = new_str.sub('', text).lower()
    return res


if __name__ == '__main__':
    st = "Геннадий, HeLP mE, 4+142"
    print(func(st))
    print(convert_str(st))