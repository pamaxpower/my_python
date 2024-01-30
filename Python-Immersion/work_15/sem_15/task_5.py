'''
Задание №5

Дорабатываем задачу 4.

Добавьте возможность запуска из командной строки.
При этом значение любого параметра можно опустить. В
этом случае берётся первый в месяце день недели, текущий
день недели и/или текущий месяц.

*Научите функцию распознавать не только текстовое
названия дня недели и месяца, но и числовые,
т.е не мая, а 5.
'''

import argparse
from task_4 import date_text
from datetime import datetime

parser = argparse.ArgumentParser(description="Принимаем строку с датой")

parser.add_argument('-cnt', type=str, default='1')
parser.add_argument('-wd', type=str, default=str(datetime.now().weekday()))
parser.add_argument('-m', type=str, default=str(datetime.now().month))


# python task_5.py -cnt=3-я -wd=среда -m=января

args = parser.parse_args()
print(args)

print(date_text(f'{args.cnt} {args.wd} {args.m}'))



