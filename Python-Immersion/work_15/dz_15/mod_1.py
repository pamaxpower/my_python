from random import randint
from time import sleep
import logging

logging.basicConfig(filename="log/t_2.log",
                    filemode='a',
                    encoding='utf-8',
                    format='{asctime} {levelname} функция "{funcName}()" строка {lineno}: {msg}',
                    style='{',
                    level=logging.INFO
                    )
logger = logging.getLogger(__name__)


def guess_game(a, b, step):
    print('Привет, давай поиграем в угадайку!\n')
    sleep(1)
    print(
        f'Правила просты: я загадал число от {a} до {b}, а ты пробуешь его угадать\n')
    sleep(1)
    print(
        f'У тебя есть {step} попыток. Я буду подсказывать тебе "больше" или "меньше"\n')
    sleep(3)
    num = randint(a, b)
    count = 1

    while count <= step:
        try:
            players_num = int(input(f'Попытка {count}. Твое число: '))
            if players_num == num:
                logger.info(
                    f'Игра закончилась. Пользователь угадал число с {count} попыток')
                print(f'\nМолодец, ты угадал число, это {num}')
                break
            elif players_num < num:
                print('Нет, моё число больше\n')
            elif players_num > num:
                print('Не угадал, мое число меньше\n')
            count += 1

            if count > step:
                logger.info('Игра закончилась. Пользователь не угадал число')
                print('Увы! ТЫ проиграл\n')
                break

        except ValueError:
            logger.error('Пользователь ввел не число')
            print('Это не целое число. Повтори ввод\n')
