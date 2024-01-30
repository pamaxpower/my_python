'''
Задание №3

Доработаем задачу 2.

Сохраняйте в лог файл раздельно:

○ уровень логирования,
○ дату события,
○ имя функции (не декоратора),
○ аргументы вызова,
○ результат.

'''

from functools import wraps
import logging
# from datetime import datetime

logging.basicConfig(
    filename="log/t_3.log",
    filemode='a',
    encoding='utf-8',
    format='{asctime} {levelname} функция "{funcName}()" строка {lineno}: {msg}',
    style='{',
    level=logging.INFO
)

# декоратор принимает на вход объект функции
def log_decor(func):

    # 
    @wraps(func)
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        logging.info(f'Функция {func.__name__}(). Аргументы: {args}. Результат: {res}')
        return res
    
    # а возвращаем объект-обертку (измененную функцию)
    return wrapper


@log_decor
def sum_x(x, y):
    return x + y

if __name__ == '__main__':
    print(sum_x(5, 2))
    print(sum_x(7, 0)) 