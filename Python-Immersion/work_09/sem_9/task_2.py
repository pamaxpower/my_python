'''
Задание №2
Дорабатываем задачу 1.

Превратите внешнюю функцию в декоратор.

Он должен проверять входят ли переданные в функцию-угадайку 
числа в диапазоны [1, 100] и [1, 10].

Если не входят, вызывать функцию со случайными числами
из диапазонов.

def main(func):
    def wrapper(*args, **kwargs):
        ...
        result = func(*args, **kwargs)
        ...
        return result
    return wrapper

@main
def my_func(data):
    ...
    return wrapper
'''
from random import randint
from typing import Callable

def deco(func: Callable):
    def wrapper(*args):
        num = args[0] if 0 < args[0] < 101 else randint(1,100)
        count = args[1] if 0 < args[1] < 11 else randint(1,10)
        return func(num, count)
    return wrapper
        


@deco
def guessing(riddle_num, count):
        #nonlocal count
        print(f'У тебя осталось {count} попыток')
        while count > 0:            
            player_name = int(input('Твое число: '))
            if riddle_num == player_name:
                return print(f'Молодец, ты угадал число, это {riddle_num}')
                
            elif player_name < riddle_num:
                print('Нет, моё число больше\n')
            elif player_name > riddle_num:
                print('Не угадал, мое число меньше\n')
            count -= 1
            print(f'У тебя осталось {count} попыток')
        return print('Увы! Ты проиграл\n')

guessing(150, 3)