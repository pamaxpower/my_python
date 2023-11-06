'''
Итераторы 
- если коллекцию можно передать в цикл for для 
последовательного перебора элементов, 
то такая коллекция итерируемая

списки, кортежи и строки возвращают элементы слева направо,
множества - в случайном порядке
'''

# функция iter(object[ ,sentinel])
# - принимает на вход объект? поддерживающий итерацию

a = 42
# iter(a) # TypeError: 'int' object is not iterable


data = [2, 4, 6, 8]
list_iter = iter(data)
print(list_iter)    # печатает объект-итератор

print(*list_iter)   # распаковка итератора
print(*list_iter)   # проходит только 1 раз


data = [2, 4, 6, 8]
# list_iter = iter(data, 6) # TypeError: iter(v, w): v must be callable

import functools

f = open('mydata.bin', 'rb')
for block in iter(functools.partial(f.read, 16), b''):
    print(block)
f.close()

