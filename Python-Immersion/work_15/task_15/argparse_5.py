'''
Добавление аргументов, add_argument

● metavar — имя, которое выводится с справке

● type — тип, для преобразования аргумента

● nargs — указывает на количество значений, которые надо собрать из
командной строки и собрать результат в список list. 
Целое число указывает количество. 
Кроме этого можно передать символ “?” — один аргумент, “*” —
все имеющиеся аргументы, “+” — все имеющиеся аргументы, но не пустое
значение.

● help - вывод подсказки об аргументе.

● action - принимает одно из строковых значений и срабатывает при 
наличии в строке вызова следующих параметров:
    * store_const - передает в args ключ со значением из 
        параметра const
    * store_true или store_false - сохраняет в ключе истину или ложь
    * append - ищет несколько появлений ключа и собрает все 
        значения после него в список
    * append_const - добавляет значение из ключа в список, 
        если ключ был вызван

'''

import argparse
def quadratic_equations(a, b, c):
    d = b ** 2 - 4 * a * c
    if d > 0:
        return (-b + d ** 0.5) / (2 * a), (-b - d ** 0.5) / (2 * a)
    if d == 0:
        return -b / (2 * a)
    return None

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Solving quadratic equations')
    
    parser.add_argument('param', metavar='a b c', type=float,
                        nargs=3, help='enter a b c separated by a space')
    args = parser.parse_args()
    print(quadratic_equations(*args.param))



