'''
Задание №3

✔ Создайте вручную кортеж содержащий элементы разных типов.
✔ Получите из него словарь списков, где:
ключ — тип элемента,
значение — список элементов данного типа.
'''

my_tuple = (1, 3.14, True, 'Hello', [1,2,3], (4,5), {6,7,8}, None)
my_dict = {}
for el in my_tuple:
    my_dict[type(el)] = el
print(my_dict)