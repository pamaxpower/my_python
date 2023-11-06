'''
LC - List comprehension
- генератор списков, списковое включение
- это не генераторное выражение 
(на выходе получается полностью готовый список с элементами)
'''

data = [2, 5, 1, 42, 65, 76, 24, 77]
res = []
for item in data:
    if item % 2 == 0:
        res.append(item)
print(f'{res = }')


data = [2, 5, 1, 42, 65, 76, 24, 77]
res = [item for item in data if item % 2 == 0]
print(f'{res = }')

# 1. Не создаём пустой список в начале.
# 2. Не пишем двоеточия после цикла и логической проверки.
# 3. Исключаем метод append.
# Итого вместо 4 строк кода получаем одну.