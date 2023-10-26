'''
Задание №4

✔ Создайте вручную список с повторяющимися элементами.
✔ Удалите из него все элементы, которые встречаются чаще двух раз.
'''

lst = [1, 5, 7, 8, 4, 5, 12, 4, 5, 12, 4, 5, 86, 2, 45, 2]

new_lst = [el for el in lst if lst.count(el) > 1]
print(list(set(lst)-set(new_lst)))

print([el for el in lst if lst.count(el) == 1])