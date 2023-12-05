'''
Дополнительные переменные в декораторе

'''
from typing import Callable


def cache(func: Callable):
    _cache_dict = {}

    def wrapper(*args):
        # проверяем наличие ключей в исходном словаре
        if args not in _cache_dict:
            # если таких ключей нет, то вызываем функцию
            _cache_dict[args] = func(*args)
        # если ключи уже имеются, то просто возвращаем словарь
        return _cache_dict[args]
    return wrapper


@cache
def factorial(n: int) -> int:
    print(f'Вычисляю факториал для числа {n}')      # сообщение, что функция начала работу
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f


print(f'{factorial(10) = }')    # функция запустится
print(f'{factorial(15) = }')    # функция запустится
print(f'{factorial(10) = }')    # просто вернет результат вычисления
print(f'{factorial(20) = }')    # функция запустится
print(f'{factorial(10) = }')    # вернет результат вычисления
print(f'{factorial(20) = }')    # вернет результат вычисления
print(f'{factorial(20) = }')
