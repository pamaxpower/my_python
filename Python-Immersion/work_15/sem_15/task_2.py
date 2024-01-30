'''
Задание №2

На семинаре про декораторы был создан логирующий
декоратор. Он сохранял аргументы функции и результат её
работы в файл.
(семинар 9 задание 3)

Напишите аналогичный декоратор, но внутри используйте
модуль logging.

'''

from functools import wraps
import logging

logging.basicConfig(
    filename="log/t_2.log",
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
        logging.info('msg')
        # logging.info(f'Функция {func}(). Аргументы {args}, {kwargs}')
        return res
    
    # а возвращаем объект-обертку (измененную функцию)
    return wrapper


@log_decor
def sum_x(x, y):
    return x + y

if __name__ == '__main__':
    print(sum_x(5, 2))
    print(sum_x(7, 0)) 