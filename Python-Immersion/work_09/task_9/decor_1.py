'''
Декоратор - структурный шаблон проектирования, предназначенный 
для динамического подключения дополнительного поведения к объекту

ДЕКОРАТОР БЕЗ ПАРАМЕТРОВ.

Передача функции в качестве аргумента

Общий вид:
def main(func):
    def wrapper(*args, **kwargs):
        ...
        result = func(*args, **kwargs)
        ...
        return result
    return wrapper

def my_func(data):
    ...
    return wrapper

deco = main(my_func)
'''

import time
from typing import Callable

# функция main принимает на вход функцию
# функция wrapper принимает некоторое количество позиционных и именнованных аргументов
# в теле функции wrapper: выводим время запуска, завершения функции и результат 
def main(func: Callable):
    def wrapper(*args, **kwargs):
        print(f'Запуск функции {func.__name__} в {time.time()}')
        result = func(*args, **kwargs)
        print(f'Результат функции {func.__name__}: {result}')
        print(f'Завершение функции {func.__name__} в {time.time()}')
        return result
    return wrapper

# используем функцию факториала числа
def factorial(n: int) -> int:
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f

# запускаем поиск факториала (проверяем функционал)
print(f'{factorial(1000) = }')      # -> получаем значение

# создаем функцию control (которая будет замыканием)
control = main(factorial)    

# проверяем имя вызываемой функции
print(f'{control.__name__ = }')     # -> переменная control содержит функцию-обертку wrapper 

# проверям значение
print(f'{control(1000) = }')        # -> покажет время запуска, завершения функции и ее результат

