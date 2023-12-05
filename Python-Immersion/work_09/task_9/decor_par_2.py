'''
Проверка
'''

import random
from typing import Callable

def count(num: int = 1):
    def deco(func: Callable):
        counter = []
        def wrapper(*args, **kwargs):
            for _ in range(num):
                result = func(*args, **kwargs)
                counter.append(result)
            return counter
        return wrapper
    return deco

@count(10)
def rnd(a: int, b: int) -> int:
    return random.randint(a, b)


print(f'{rnd(1, 10) = }')       # список из одного случайного числа от 1 до 10
print(f'{rnd(1, 100) = }')      # список из певрого числа и случайного числа от 1 до 100
print(f'{rnd(1, 1000) = }')     # список из двух первых чисел и случайного числа от 1 до 1000


# Ответ:
# Мой ответ не верный 
# Правильный ответ:
# 1) список из 10 случайных чисел от 1 до 10
# 2) список из первых 10 случайных чисел + 10 случайных числа от 1 до 100
# # 3) первые 20 чисел + 10 случайных чисел от 1 до 1000

# Если бы список counter был создан в функции wrapper, 
# то получили бы 3 разных списков из 10 случайных чисел
