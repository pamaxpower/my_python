'''
Аргумент:
1) изменяемый - при изменении внутри функции, изменяется и за ее пределами
2) неизменяемый - при изменении внутри функции, остается прежним вне функции

'''

# Неизменяемый аргумент

def no_mutable(num: int) -> int:
    num += 1
    print(f'In func {num = }')
    return num

a = 42
print(f'In main {a = }')
z = no_mutable(a)
print(f'{a = }\t{z = }')

# Изменяемый аргумент

def mutable(data: list[int]) -> list[int]:
    for i, item in enumerate(data):
        data[i] = item + 1
    print(f'In func {data = }')
    return data

my_list = [2, 4, 6, 8]
print(f'In main {my_list = }')
new_list = mutable(my_list)
print(f'{my_list = }\t{new_list = }')

# Вывод: если аргументом функции передали неизменяемый объект, 
# то он не изменится.
# Если же аргументом является изменяемый объект 
# (список, множество, словарь), то и после вызова 
# функции он поменяется