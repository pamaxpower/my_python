'''
Задание №5

Объедините функции из прошлых задач.

Функцию угадайку задекорируйте:

- декораторами для сохранения параметров,
- декоратором контроля значений и
- декоратором для многократного запуска.

Выберите верный порядок декораторов.
'''

from task_3 import decor
from task_4 import f_count


@f_count(5)
@decor
def guessing(riddle_num, count):
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


guessing(45, 5)