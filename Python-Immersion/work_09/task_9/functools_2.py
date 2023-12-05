'''ДЕКОРАТОРЫ МОДУЛЯ FUNCTOOLS

Декоратор cache
- позволяет кэшировать результат работы функции

@cache
def my_func(data):
    ...  
'''

from functools import cache

@cache
def factorial(n: int) -> int:
    print(f'Вычисляю факториал для числа {n}')
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f


print(f'{factorial(10) = }')
print(f'{factorial(15) = }')
print(f'{factorial(10) = }')
print(f'{factorial(20) = }')
print(f'{factorial(10) = }')
print(f'{factorial(20) = }')
# Функция запускает функцию факториала и вычисляет его значение, 
#но если fhuevtyn повторяется, то функция не запускается, 
# а просто возвращается ее результат