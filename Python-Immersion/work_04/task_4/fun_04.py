'''
Аргументы функции. Значения по умолчанию

def my_func(a, b=0, c=0):
    pass
    
1) При вывове функции можно передать 1 аргумент a, 
остальные аргументы, по умолчанию, будут равны 0

2) если аргументам b и c передать значению, 
то функция будет использовать переданные значения

В качестве значений по умолчанию, могут использоваться 
только неизменяемые типы данных
'''


def quadratic_equations(a, b=0, c=0):
    d = b ** 2 - 4 * a * c
    if d > 0:
        return (-b + d ** 0.5) / (2 * a), (-b - d ** 0.5) / (2 * a)
    if d == 0:
        return -b / (2 * a)


print(quadratic_equations(5))   # -> 0.0

print(quadratic_equations(5, 3))   # -> (0.0, 0.6)

print(quadratic_equations(2, 7, 3))   # -> (-0.5, -3.0)


def from_one_to_n(n, data=[]):
    for i in range(1, n + 1):
        data.append(i)
    return data


new_list = from_one_to_n(5)
print('\n', f'{new_list = }')
other_list = from_one_to_n(7)
print(f'{other_list = }', '\n')

# other_list содержит в себе и новую последовательность и ту,
# которая была в списке new_list.
# Связано это с тем, что значение по умолчанию задаётся один
# раз при создании функции.

# чтобы этого избежать, в качестве аргумента по умолчанию
# передается None, а пустой список создается уже в теле функции


def from_one_to_n2(n, data=None):
    if data is None:
        data = []
    for i in range(1, n + 1):
        data.append(i)
    return data


new_list = from_one_to_n2(5)
print(f'{new_list = }')
other_list = from_one_to_n2(7)
print(f'{other_list = }')
