'''
Методы списков. Добавление элементов
'''
# .append()

a = 42
b = 'Hello world'
c = [1, 3, 5, 7]
mylist = [None]
mylist.append(a)
print(mylist)
mylist.append(b)
print(mylist)
mylist.append(c)
print(mylist)

# .extend() - не работает с одним объектом.
# последовательно добавляет каждый элемент 
# последовательности в список

mylist2 = [None]
# mylist2.extend(a)
print(mylist2)      # TypeError: 'int' object is not iterable
mylist2.extend(b)
print(mylist2)
mylist2.extend(c)
print(mylist2)