'''
Словари - набор пар (ключ, значение)
'''

# Инициализация
# dict_1 = dict(x)
# dict_2 = {key: value}
a = {'one': 42, 'two': 3.14, 'ten': 'Hello world!'}
b = dict(one=42, two=3.14, ten='Hello world!')
c = dict([('one', 42), ('two', 3.14), ('ten', 'Hello world!')])
print(a == b == c)

# Добавление элементов
x = 3
a['three'] = x
print(a)
