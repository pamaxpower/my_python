"""Генераторные выраждения для словарей и множеств"""


my_set = {el**3 for el in range(5, 10)}
print(my_set)  # -> {512, 343, 216, 729, 125}


my_set = set()
for el in range(5, 10):
    my_set.add(el**2)
print(my_set)

my_set = {el**2 for el in range(5, 10)}
print(my_set)

my_dict = {el: el**2 for el in range(5, 10)}
print(my_dict)
