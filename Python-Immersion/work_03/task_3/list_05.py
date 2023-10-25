'''
Методы списков.
'''

# .count() - подсчет числа вхождений в список

lst = [2, 4, 6, 2, 8, 10, 12, 2, 4, 14, 2]
spam = lst.count(2)
eggs = lst.count(3)
print(spam, eggs)
print()

# .index() - возвращает индекс первого вхождения

s1 = lst.index(4)
print(s1)
eggs = lst.index(4, s1 + 1, 90)
print(eggs)
# err = lst.index(3)      # ValueError: 3 is not in list
print()

# .insert() - вставка значний по индексу

lst.insert(2, 555)
print(lst)
lst.insert(-2, 13)
print(lst)
lst.insert(42, 73)       # lst.append(73)
print(lst, '\n')

# .remove() - удаление элемента по значению

lst.remove(6)
print(lst)
# lst.remove(3)   # ValueError: list.remove(x): x not in list
print(lst)
