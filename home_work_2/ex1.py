"""
Создать список и заполнить его элементами различных типов данных.
Реализовать проверку типа данных каждого элемента.
Использовать функцию type() для проверки типа.
Элементы списка можно не запрашивать у пользователя, а указать явно,
в программе.
"""

my_list = [7, "учеба", 0.33, False, None]

# for i in range(len(my_list)):
#     print(my_list[i], '=', type(my_list[i]))

for el in my_list:
    print(type(el))

# for j in range(len(my_list)):
#     print(type(my_list[j]))
