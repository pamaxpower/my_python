'''
Сортировка элементов
'''
lst = [4, 8, 2, 9, 1, 7, 2]

# sorted() - сортирует список, не меняя старый. Создает новый

sort_lst = sorted(lst)
print(lst, sort_lst, sep='   ')
rev_lst = sorted(lst, reverse=True)
print(lst, rev_lst, sep='   ')
print()

# .sort() - списочный метод, изменяет текущий список.
# не работает на строках

lst.sort()
print(lst)
lst.sort(reverse=True)
print(lst, '\n')


# reversed() - разворот списка

# объект-генератор, который генерирует список справа налево
res = reversed(lst)
print(type(res), res)
res_rev_list = list(reversed(lst))
print(type(res_rev_list), res_rev_list)
print()

# .reverse() - разворачивает элементы списка, не создавая новый объект
lst.reverse()
print(lst)
new_lst = lst[::-1]
print(lst, new_lst, sep='   ')
