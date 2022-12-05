"""
Сортировка массива
"""
# перемешивание
import random

n = int(input('Размер списка: '))
mylist = []
for i in range(n):
    mylist.append(i)

print(mylist)

new_list = []
for j in range(0, len(mylist)):
    j = random.randrange(0, len(mylist))
    new_list.append(mylist[j])
    mylist.remove(mylist[j])
print(new_list)