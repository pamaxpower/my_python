'''
Задание №1

Напишите программу, которая использует модуль logging для
вывода сообщения об ошибке в файл.

Например отлавливаем ошибку деления на ноль.
'''

import logging

logging.basicConfig(
    filename="log/t_1.log",
    filemode='a',
    encoding='utf-8',
    format='{asctime} {levelname} функция "{funcName}()" строка {lineno}: {msg}',
    style='{',
    level=logging.ERROR
)

logger = logging.getLogger(__name__)


def div(a, b):
    try:
        res = a / b
    except ZeroDivisionError:
        logger.error('Поймали ошибку ZeroDivisionError. На 0 делить нельзя')
        logger.info('Для примера')      # будет выводиться, если level=logging.info
        return float('inf')
    return res


if __name__ == '__main__':
    print(div(5, 2))
    print(div(7, 0))
