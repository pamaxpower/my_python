'''
Задание №1
Создайте функцию-замыкание, которая запрашивает два целых
числа:

от 1 до 100 для загадывания,
от 1 до 10 для количества попыток

Функция возвращает функцию, которая через консоль просит
угадать загаданное число за указанное число попыток.
'''

from typing import Callable

def riddle(riddle_num, count):

    def guessing():
        nonlocal count
        print(f'У тебя осталось {count} попыток')
        while count > 0:            
            player_name = int(input(f'Твое число: '))
            if riddle_num == player_name:
                return print(f'Молодец, ты угадал число, это {riddle_num}')
                
            elif player_name < riddle_num:
                print('Нет, моё число больше\n')
            elif player_name > riddle_num:
                print('Не угадал, мое число меньше\n')
            count -= 1
            print(f'У тебя осталось {count} попыток')
        return print('Увы! ТЫ проиграл\n')
        
    return guessing
        
res = riddle(45, 5)
res()