'''
Задание №7

✔ Функция получает на вход словарь с названием компании в качестве ключа
и списком с доходами и расходами (3-10 чисел) в качестве значения.
✔ Вычислите итоговую прибыль или убыток каждой компании. Если все компании
прибыльные, верните истину, а если хотя бы одна убыточная — ложь.
'''

# data = {
#     'Apple': (145, 75, -32, 48),
#     'SpaceX': (250, 480, 1500),
#     'Tesla': (360, 940, 810)
#     }

data = {"company_1": [70, 12, 25, -28, 10, 36],
        "company_2": [-55, 10, -20, -10, -15, -15],
        "company_3": [40, 12, 21, -70, 11, 65]}


def renta(dct: dict):
    res = {}
    for key, value in dct.items():
        res[key] = sum(value)
    return all(map(lambda x: x > 0, res.values()))


print(renta(data))


def renta_2(dct):
    for el in dct.values():
        if sum(el) < 0:
            return False
    return True

print(renta_2(data))
