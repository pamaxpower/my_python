'''
Дан список повторяющихся элементов lst. 
Вернуть список с дублирующимися элементами. 
В результирующем списке не должно быть дубликатов.
'''
lst = [1, 1, 2, 2, 3, 3]

print(list(set([el for el in lst if lst.count(el) > 1])))