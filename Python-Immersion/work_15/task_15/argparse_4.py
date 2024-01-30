'''
Выгрузка результатов, parse_args

принимает два аргумента на вход:

* строку для анализа (по умолчанию sys.args)
* объект для хранения результатов? по умолчанию класс Namespace(Object)


'''
import argparse

parser = argparse.ArgumentParser(description='My first argument parser')
parser.add_argument('numbers', metavar='N', type=float,
                    nargs='*', help='press some numbers')
args = parser.parse_args()

print(f'Получили экземпляр Namespace: {args = }')
print(f'У Namespace работает точечная нотация: {args.numbers =}')
print(f'Объекты внутри могут быть любыми: {args.numbers[1] = }')

# python argparse_4.py 42 3.14 73 