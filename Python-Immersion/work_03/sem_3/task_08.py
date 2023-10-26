'''
Задание №8

✔ Три друга взяли вещи в поход. Сформируйте
словарь, где ключ — имя друга, а значение —
кортеж вещей. Ответьте на вопросы:
✔ Какие вещи взяли все три друга
✔ Какие вещи уникальны, есть только у одного друга
✔ Какие вещи есть у всех друзей кроме одного
и имя того, у кого данная вещь отсутствует
✔ Для решения используйте операции
с множествами. Код должен расширяться
на любое большее количество друзей.
'''

data = {
    "Вася": ("Палатка", "Котелок", "Спички", "Шашлык"),
    "Витя": ("Палатка", "Котелок", "Топор"),
    "Петя": ("Палатка", "Котелок", "Топор", "Спирт"),
    "Саша": ("Палатка", "Спирт")
}

# Какие вещи взяли все друзья 

lst = []
for k, v in data.items():
    lst.append(set(v))
print(lst)

for i in range(len(lst) - 2):
    res_all = lst[i].intersection(lst[i + 1])
    res_all = res_all.intersection(lst[i + 2])

print(res_all)

# Какие вещи уникальны, есть только у одного друга

my_set = set()
for el in data:
    my_set = set(data[el])
    for el_1 in data:
        if el != el_1:
            my_set = my_set.difference(set(data[el_1]))
    if my_set:
        print(el, my_set)

# Какие вещи есть у всех друзей кроме одного
# и имя того, у кого данная вещь отсутствует

for s in data:
    my_set = set(data[s])
    my_set_new = set()
    for f in data:
        if s != f:
            my_set_new = my_set_new.intersection(set(data[f])) if my_set_new else set(data[f])
    if my_set_new:
        delta = my_set_new.difference(my_set)
        if delta:
            print(s, delta)
