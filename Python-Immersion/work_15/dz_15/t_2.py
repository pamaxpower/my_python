'''
Дополнтельная задача #1

Возьмите любые 1-3 задания из прошлых домашних заданий. 

Добавьте к ним логирование ошибок и полезной информации. 

Также реализуйте возможность запуска из командной строки с передачей параметров. 


Возьму игру угадайку из 6 урока. Сама угадайка находится в файле mod_1.py

'''
import argparse
from mod_1 import guess_game

parser = argparse.ArgumentParser(description="Принимаем строку с датой")

parser.add_argument('-m', type=int, help='Введите нижнюю границу диапазона',
                    default='1')
parser.add_argument('-l', type=int, help='Введите верхнюю границу диапазона',
                    default='1')
parser.add_argument('-c', type=int, help='Введите количество попыток',
                    default='1')

args = parser.parse_args()

if __name__ == '__main__':
    guess_game(args.m, args.l, args.c)
