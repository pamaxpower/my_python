'''
Проверка на вхождение IN

Линейное время: O(n)
obj in list
obj in tuple
sub_str in str

Константное время:  O(1)
key in dict
obj in set
obj in frozenset
'''

my_set = frozenset({3, 4, 1, 2, 5, 6, 1, 7, 2, 7})
print(len(my_set))
print(my_set - {1, 2, 3})
print(my_set.union({2, 4, 6, 8}))
print(my_set & {2, 4, 6, 8})
# print(my_set.discard(10))       # AttributeError: 'frozenset' object has no attribute 'discard'
