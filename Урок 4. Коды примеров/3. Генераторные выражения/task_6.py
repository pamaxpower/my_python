"""Генераторы списков и словарей"""

# генераторное выражение с условием
my_list = [10, 25, 30, 45, 50]

new_list = [el for el in my_list if el % 2 == 0]
print(new_list)

