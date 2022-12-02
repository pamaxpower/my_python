'''
Множества
- содержит в себе уникальные элементы (как упорядоченные, так и нет)
'''

# colors = {'red', 'green', 'blue'}
# print(type(colors))             # класс set - тип множество

# # Добавление элементов
# colors.add('red')           # ничего не произойдет - элемент уже есть
# colors.add('gray')          # {'gray', 'red', 'green', 'blue'}
# print(colors)

# # Удаление элементов
# colors.remove('red')          # {'blue', 'gray', 'green'}
# colors.remove('red')          # KeyError: 'red' - такого элемента уже нет
# colors.discard('red')         # Удаление элемента. И если его нет, то ошибки не будет
# print(colors)

# colors.clear()                # очистка множества (на выходе пустое множество) set()

# Операции с множествами:

a = {1, 2, 3, 5, 8}
b = {2, 5, 8, 13, 21}
c = a.copy()                # Копия множества {1, 2, 3, 5, 8} 
u = a.union(b)              # Объединение множетсв: {1, 2, 3, 5, 8, 13, 21}
i = a.intersection(b)       # Пересечение множеств: {8, 2, 5}
dl = a.difference(b)        # {1, 3}
dr = b.difference(a)        # {13, 21}

q = a \
    .union(b) \
    .difference(a.intersection(b))
# {1, 21, 3, 13}

s = frozenset(a)            # сделать множество неизменяемым (заморозить его)

