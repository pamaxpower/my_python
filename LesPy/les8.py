"""
List Comprehension - механизм быстрого создания списков

[exp for item in iterable] - записываем выражение, получаемое перебором элементов какого-то итерируемого объекта

[exp for item in iterable (if conditional)] - записываем выражение, соответствующее условию (if conditional) и получаемое перебором элементов какого-то итерируемого объекта

[exp <if conditional> for item in iterable (if conditional)]

"""

# # обычное создание списка с помощью цмкла for
# mylist = []
# for i in range(1, 21):
#     if i % 2 == 0:
#         mylist.append(i)

mylist1 = [i for i  in range(1, 21) if i % 2 == 0]    # создаем список четных элементов от 1 до 20
print(mylist1)

mylist2 = [(i, i) for i  in range(1, 21) if i % 2 == 0]     # список кортежей
print(mylist2)

def f(x):
    return x**3
mylist3 = [(i, f(i)) for i  in range(1, 21) if i % 2 == 0]      # в качестве выражения может принимать функцию
print(mylist3)


