'''
Методы списков. Удаление элементов
'''

# .pop() - удаляет элемент из списка,
# попутно сохраняя его в переменной

my_list = [2, 4, 6, 8, 10, 12]

spam = my_list.pop()        # удаляет последний элемент
print(spam, my_list)
eggs = my_list.pop(1)       # удаляет элемент по индексу
print(eggs, my_list)
# err = my_list.pop(10)       # IndexError: pop index out of range
