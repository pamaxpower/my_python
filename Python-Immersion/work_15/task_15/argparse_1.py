'''
Модуль argparse
- запуск скриптов с параметрами 
- надстраивается над sys.argv
- генерирует справку, определяет способ анализа аргументов 
каждой строки и сообщает об ошибках

'''
import argparse

parser = argparse.ArgumentParser(description='My first argument parser')

parser.add_argument('numbers', metavar='N', type=float,
                    nargs='*', help='press some numbers')

# numbers - имя списка
# metavar - обозначение выводится в справке
# type - какие нужны аргументы (к этому типу приведутся введенные данные)
# nargs - сколько бы не получили аргументов из них надо составить список


args = parser.parse_args()

print(f'В скрипт передано: {args}')

# Ввод в консоль
# python argparse_1.py 42 3.14 73           # В скрипт передано: Namespace(numbers=[42.0, 3.14, 73.0])
# python argparse_1.py 42 --help            # вывод справки 
# python argparse_1.py 42 Hello world!      # error: argument N: invalid float value: 'Hello'

