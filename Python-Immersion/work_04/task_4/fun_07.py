'''
Области видимости

1) Локальная - только внутри функции (переменные заданные в теле функции)

2) Глобальная (global) - код модуля, переменные заданы в общем файле, 
содержащем функцию

3) Не локальная (nonlocal) - код функции, исключающий доступ к 
глобальным переменным
'''

#  Локальные переменные:
def func(y: int) -> int:
    x = 100
    print(f'In func {x = }')
    return y + 1

x = 42
print(f'In main {x = }')
z = func(x)
print(f'{x = }\t{z = }', '\n')


# Глобальные переменные:
def func_2(y: int) -> int:
    global x
    x += 100
    print(f'In func {x = }')    # 42 + 100
    return y + 1

x = 42
print(f'In main {x = }')
z = func_2(x)
print(f'{x = }\t{z = }', '\n')


# Не локальные переменные:
def main(a):
    x1 = 1

    def func_3(y):
        nonlocal x1
        x1 += 100       # 1 + 100
        print(f'In func {x1 = }')
        return y + 1
    
    return x1 + func_3(a)

x1 = 42
print(f'In main {x1 = }')
z = main(x1)        # 42 + 1 + 1
print(f'{x1 = }\t{z = }', '\n')


# Константы
LIMIT = 1_000

def func_4(x, y):
    result = x ** y % LIMIT
    return result

print(func_4(42, 73))
