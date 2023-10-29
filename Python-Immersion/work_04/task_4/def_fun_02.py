'''
Встроенные функции. Часть 2.

max(iterable, *[, key, default])
max(arg1, arg2, *args[, key])
- функция принимает на вход итерируемую последовательность 
или несколько аргументов и находит макисмальных из них

min(iterable, *[, key, default])
min(arg1, arg2, *args[, key])
- тоже самое что и max, но только ищет минимальный элемеент

sum(iterable, /, start=0)
- функция принимает объект итератор и 
подсчитывает сумму всех элементов.
Ключевой аргумент staке задает начальное 
значение для суммирования

'''

lst_1 = []
lst_2 = [42, 256, 73]
lst_3 = [("Иван", 125_000), ("Николай", 96_000), ("Пётр",
109_000)]
print(max(lst_1, default='empty'))
print(max(*lst_2))
print(max(lst_3, key=lambda x: x[1]))
print()

print(min(lst_1, default='empty'))
print(min(*lst_2))
print(min(lst_3, key=lambda x: x[1]))
print()

my_list = [42, 256, 73]
print(sum(my_list))
print(sum(my_list, start=1024))