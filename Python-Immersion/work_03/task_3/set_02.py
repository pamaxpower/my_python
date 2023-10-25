'''
Работа с множествами
'''

# add() - добавление элементов

my_set = {3, 4, 2, 5, 6, 1, 7}
my_set.add(9)
print(my_set)
my_set.add(7)
print(my_set)
# my_set.add(9, 10) # TypeError: set.add() takes exactly one argument (2 given)
my_set.add((9, 10))
print(my_set, '\n')

# remove() - удаление элемента

my_set = {3, 4, 2, 5, 6, 1, 7}
my_set.remove(5)
print(my_set, '\n')
# my_set.remove(10) # KeyError: 10

# discard() - удаление элемента

my_set = {3, 4, 2, 5, 6, 1, 7}
my_set.discard(5)
print(my_set, '\n')
my_set.discard(10)  # значения нет, но запрос игнорируется, ошибки не будет

# intersection() - пересечение множеств, &

my_set = {3, 4, 2, 5, 6, 1, 7}
other_set = {1, 4, 42, 314}
new_set = my_set.intersection(other_set)
print(f'{my_set = }\n{other_set = }\n{new_set = }')
new_set_2 = my_set & other_set
print(f'{new_set_2 = }\n')

# union() - объединение множеств, |

my_set = {3, 4, 2, 5, 6, 1, 7}
other_set = {1, 4, 42, 314}
new_set = my_set.union(other_set)
print(f'{my_set = }\n{other_set = }\n{new_set = }')
new_set_2 = my_set | other_set
print(f'{new_set_2 = }\n')

# difference() - разность множеств, -

my_set = {3, 4, 2, 5, 6, 1, 7}
other_set = {1, 4, 42, 314}
new_set = my_set.difference(other_set)
print(f'{my_set = }\n{other_set = }\n{new_set = }')
new_set_2 = my_set - other_set
print(f'{new_set_2 = }\n')
