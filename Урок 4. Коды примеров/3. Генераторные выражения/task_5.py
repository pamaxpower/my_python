"""Генераторы списков и словарей"""

# традиционный итератор с ф-цией append
my_lst = [1, 2, 3, 4, 5]
res = []
for el in my_lst:
    res.append(el**2)

print(res)

# списковое включение (генераторные выражение)
res = [el**2 for el in my_lst]
print(res)
