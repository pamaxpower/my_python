from random import randint 
from time import sleep

def guess_game(a, b, step):
    print('Привет, давай поиграем в угадайку!\n')
    sleep(1)
    print(f'Правила просты: я загадал число от {a} до {b}, а ты пробуешь его угадать\n')
    sleep(1)
    print(f'У тебя есть {step} попыток. Я буду подсказывать тебе "больше" или "меньше"\n')
    sleep(3)
    num = randint(a,b)
    count = 1
    
    while count <= step:
        players_num = int(input(f'Попытка {count}. Твое число: '))
        sleep(3)
        

        if players_num == num:
            print(f'\nМолодец, ты угадал число, это {num}')
            break
        elif players_num < num:
            print('Нет, моё число больше\n')
        elif players_num > num:
            print('Не угадал, мое число меньше\n')
        count += 1

        if count > step:
            print('Увы! ТЫ проиграл\n')
            break

        