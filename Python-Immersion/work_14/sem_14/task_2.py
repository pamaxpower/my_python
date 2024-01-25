'''
Задание №2

Напишите для задачи 1 тесты doctest. Проверьте
следующие варианты:
* возврат строки без изменений
* возврат строки с преобразованием регистра без потери
* символов
* возврат строки с удалением знаков пунктуации
* возврат строки с удалением букв других алфавитов
* возврат строки с учётом всех вышеперечисленных пунктов
(кроме п. 1)
'''
import re 

def func(text):
    """
    Удаляет из текста все символы, кроме
    букв латинского алфавита и пробелов
    >>> func('hello')
    'hello'

    >>> func('YoU mY bRoTHer')
    'you my brother'

    >>> func('hello world!!!')
    'hello world'

    >>> func('Валера cool')
    ' cool'

    >>> func('100 раз YoU говорю!')
    '  you '
    """
    result = ''
    for el in text:
        if el.isalpha() and 'a' <= el.lower() <= 'z' or el.isspace():
            result += el.lower()
    return result


# def convert_str(text):
#     """
#     Удаляет из текста все символы, кроме
#     букв латинского алфавита и пробелов

#     >>> func('hello')
#     'hello'

#     >>> func('YoU mY bRoTHer')
#     'you my brother'

#     >>> func('hello world!!!')
#     'hello world'

#     >>> func('Валера cool')
#     ' cool'

#     >>> func('100 раз YoU говорю!')
#     '  you '
#     """
#     new_str = re.compile('[^a-zA-Z ]')
#     res = new_str.sub('', text).lower()
#     return res


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
