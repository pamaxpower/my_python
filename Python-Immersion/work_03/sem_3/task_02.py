'''
Задание №2

Пользователь вводит данные. Сделайте проверку данных
и преобразуйте если возможно в один из вариантов ниже:
✔ Целое положительное число
✔ Вещественное положительное или отрицательное число
✔ Строку в нижнем регистре, если в строке есть
хотя бы одна заглавная буква
✔ Строку в нижнем регистре в остальных случаях
'''


data = input('Введите данные: ')

if data.isdigit():
    print('1', int(data))
elif data.replace(',', '').isdigit() or data.replace('.', '').isdigit():
    print('2', float(data.replace(',', '.')))
elif data.startswith('-'):
    print('2', float(data))
elif any([el.isupper() for el in data]):
    print('3', data.upper())
else:
    print('4', data.lower())


# txt = 'Привет'
# for el in txt:
#     if el.isupper():
#         print('+')


# print([for el in txt if el.isupper()])
# # print(el.isupper() for el in txt)