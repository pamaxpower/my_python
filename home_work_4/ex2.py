"""
Представлен список чисел. Необходимо вывести элементы исходного списка,
значения которых больше предыдущего элемента.

Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
Для формирования списка использовать генератор.

Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].

Результат: [12, 44, 4, 10, 78, 123].

"""

import random

#n = int(input('Размер списка: '))
#mylist = []
#for i in range(n):                  # генерируем случайный список
#    x = random.randrange(0, 1000)
#    mylist.append(x)
#
#print(mylist)

mylist = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
mylist2 = [5, 4, 3, 2, 1, 0]
new_list = []
for j in range(1, len(mylist)-1):   # формируем новый список по условию
    if mylist[j] > mylist[j-1]:
        new_list.append(mylist[j])

print(f'Первый способ: {new_list}')


def larger_item(lst):
    return [lst[j] for j in range(1, len(lst)-1) if lst[j] > lst[j-1]]


print(f'Второй способ: {larger_item(mylist)}')
print(f'Второй способ: {larger_item(mylist2)}')
print(bool(larger_item(mylist2)))

