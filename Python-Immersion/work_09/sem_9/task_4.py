'''
Задание №4

Создайте декоратор с параметром.

Параметр - целое число, количество запусков декорируемой
функции.
'''
from functools import wraps


def f_count(num: int = 1):
    
    def decor(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            count = 1
            for _ in range(num):
                print(f'\n{count} запуск')
                res = func(*args, **kwargs)
                count += 1
            return res, num
        return wrapper
    return decor

@f_count()
def summ(x, y):
    return x + y



if __name__ == "__main__":
    print(summ(10, 2))


# result = f_count(10)(summ)
# print(result(15, 3))

