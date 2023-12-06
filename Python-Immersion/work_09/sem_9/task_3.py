'''
Задание №3

Напишите декоратор, который сохраняет в json файл
параметры декорируемой функции и результат, который она
возвращает. При повторном вызове файл должен
расширяться, а не перезаписываться.

Каждый ключевой параметр сохраните как отдельный ключ
json словаря.

Для декорирования напишите функцию, которая может
принимать как позиционные, так и ключевые аргументы.
Имя файла должно совпадать с именем декорируемой
функции.

'''
from json import dump
from functools import wraps

def decor(func):
    my_dict = {}
    @wraps(func)
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        file_name = f'{func.__name__}.json'
        my_dict['arguments'] = f'{args[0], args[1]}'
        my_dict['result'] = res
        with open(file_name, 'a', encoding='utf-8') as js_f:
            dump(my_dict, js_f, indent=2)
        return res
    return wrapper

@decor
def power_x(x, y):
    return x ** y

if __name__ == "__main__":
    print(power_x(5, 3))