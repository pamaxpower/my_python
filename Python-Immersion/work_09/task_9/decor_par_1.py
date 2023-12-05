'''
ДЕКОРАТОРЫ С ПАРМЕТРАМИ

Общий вид:
def  count(param):
    def deco(func: Callable):
        def wrapper(*args, **kwargs):
            ...
            return result
        return wrapper
    return deco

Верхний уровень: нужен для приема параметров декоратора
Средний уровень: прием функции, которую мы декорируем
Нижний уровень: сама работа декоратор
'''

import time
from typing import Callable

def count(num: int = 1):            # принимает целое число 
    def deco(func: Callable):
        def wrapper(*args, **kwargs):
            time_for_count = []
            result = None
            for _ in range(num):
                start = time.perf_counter()             # начало замера
                result = func(*args, **kwargs)          # вычисление 
                stop = time.perf_counter()              # конец замера
                time_for_count.append(stop - start)     # время выполнения
            print(f'Результаты замеров {time_for_count}')   # список замеров
            return result
        return wrapper
    return deco

@count(3)
def factorial(n: int) -> int:
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f

print(f'{factorial(1000) = }')
print(f'{factorial(1000) = }')

