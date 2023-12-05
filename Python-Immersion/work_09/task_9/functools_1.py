'''
ДЕКОРАТОРЫ МОДУЛЯ FUNCTOOLS

Декоратор wraps

Общий вид:
def  count(param):
    def deco(func: Callable):
        @wraps(func)
        def wrapper(*args, **kwargs):
            ...
            return result
        return wrapper
    return deco

__name__ получает имя декорируемой функции
help() - справка
'''

import random
from functools import wraps
from typing import Callable

def count(num: int = 1):
    def deco(func: Callable):
        counter = []
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num):
                result = func(*args, **kwargs)
                counter.append(result)
            return counter
        return wrapper
    return deco

@count(10)
def factorial(n: int) -> int:
    """Returns the factorial of the number n."""
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f


print(f'{factorial(1000) = }')
print(f'{factorial.__name__ = }')
help(factorial)

