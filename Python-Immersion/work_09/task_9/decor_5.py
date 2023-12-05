'''
Проверка
'''
import random
from typing import Callable

def cache(func: Callable):
    _cache_dict = {}
    def wrapper(*args):
        if args not in _cache_dict:
            _cache_dict[args] = func(*args)
        return _cache_dict[args]
    return wrapper

@cache
def rnd(a: int, b: int) -> int:
    return random.randint(a, b)

print(f'{rnd(1, 10) = }')   # вернет случайное число от 1 до 10
print(f'{rnd(1, 10) = }')   # вернет то же число (т.к. новый вызов функции не запустится)
print(f'{rnd(1, 10) = }')   # вернет то же число

# Ответы:
# Верно