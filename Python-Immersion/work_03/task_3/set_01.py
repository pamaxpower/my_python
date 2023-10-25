'''
Множества (set и frezenset) 
- коллекция, которая содержит уникальные значения (без повторов)

my_set = {1,2,3,4,5,6,7}                - изменяемое 
my_f_set = frozenset((1,2,3,4,5,6,7,))  - неизменяемое
'''

my_set = {1, 2, 3, 4, 5, 6, 7}
print(my_set)
my_f_set = frozenset((1, 2, 3, 4, 5, 6, 7,))
print(my_f_set)
# not_set = {1, 2, 3, 4, 5, 6, 7, ['a', 'b']} # TypeError: unhashable type: 'list'
