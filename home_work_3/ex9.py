"""
Задайте список из вещественных чисел. Напишите программу, которая найдёт
разницу между максимальным и минимальным значением дробной части элементов.

Пример:

- [1.1, 1.2, 3.1, 5, 10.01] => 0.19
"""

n = int(input('Введите количество элементов: '))
my_list = []
for i in range(n):                          
    my_list.append(float(input(f'Введите {i} элемент: ')))


res = []
for i in range(len(my_list)):
    x = my_list[i] - int(my_list[i])    # находим дробную часть
    res.append(x)                       # добавляем ее в новый
    print(res)

total = max(res) - min(res)             # находим min и max и складываем их

print(round(total, 2))
