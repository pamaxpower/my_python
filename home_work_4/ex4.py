"""
Представлен список чисел. Определить элементы списка, не имеющие повторений. 
Сформировать итоговый массив чисел, соответствующих требованию. 
Элементы вывести в порядке их следования в исходном списке.
Для выполнения задания обязательно использовать генератор.
Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
Результат: [23, 1, 3, 10, 4, 11]
"""

mylist = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
mylist2 = [3, 2, 1]


def unique_items(lst):
    return [el for el in lst if lst.count(el) == 1]


print(unique_items(mylist))
print(unique_items(mylist2))
print(bool(unique_items(mylist2)))

res = []
for el in mylist:
    if mylist.count(el) == 1:
        res.append(el)
print(res)
