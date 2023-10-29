'''
Параметры *args, **kwargs

def func(*args) - принимает любое число позиционных аргументов
def func(**kwargs) - принимает любое число ключевых аргументов
def func(*args, **kwargs) - принимает любое число позиционных и ключевых аргументов

'''

def mean(args):
    return sum(args) / len(args)

print(mean([1, 2, 3]), '\n')
# print(mean(1, 2, 3)) # TypeError: mean() takes 1 positional

# Со списком данная функция будет работать, 
# а во втором случае функция считает, 
# что введено 3 аргумента, а функция должна принимать 1


def mean_2(*args):
    # Параметр *args превращается в кортеж
    return sum(args) / len(args)

print(mean_2(*[1, 2, 3]))
print(mean_2(1, 2, 3), '\n')


def school_print(**kwargs):
    # При работе **kwargs превращается в словарь
    for key, value in kwargs.items():
        print(f'По предмету "{key}" получена оценка {value}')

school_print(химия=5, физика=4, математика=5, физра=5)
