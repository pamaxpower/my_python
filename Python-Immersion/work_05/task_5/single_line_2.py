'''
Упаковка и распаковка
'''


# Упаковка и распаковка значений
a, b, c = "один", "два", "три"    # если больше или меньше трех символов, то будет ошибка ValueError
print(f'{a=} {b=} {c=}')


# Распаковка коллекция с упаковкой лишнего
data = ["один", "два", "три", "четыре", "пять", "шесть", "семь", ]
a, b, c, *d = data      # первые 3 в переменные a,b,c, остальное в d
print(f'{a=} {b=} {c=} {d=}')

a, b, *c, d = data      # 1 и 2 в a,b, последний - в d, остальное в c
print(f'{a=} {b=} {c=} {d=}')

a, *b, c, d = data      # первый в a, два последних в - c,d, остальное - в b
print(f'{a=} {b=} {c=} {d=}')

*a, b, c, d = data      # последние в b,c,d, остальное в a
print(f'{a=} {b=} {c=} {d=}')


link ='https://docs.python.org/3/faq/programming.html#how-can-i-pass-optional-or-keyword-parameters-from-one-function-to-another'
prefix, *_, suffix = link.split('/')    # разделяет на переменные до первой / и после последней /, остальное сбрасывает в ненужную переменную _
print(prefix, suffix)


# Распаковка со звездочкой
data = [2, 4, 6, 8, 10, ]
for item in data:
    print(item, end='\t')
print()

data = [2, 4, 6, 8, 10, ]
print(*data, sep='\t')      # короткая запись