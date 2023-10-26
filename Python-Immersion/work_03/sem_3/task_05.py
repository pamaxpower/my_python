'''
Задание №5

✔ Создайте вручную список с повторяющимися целыми числами.
✔ Сформируйте список с порядковыми номерами
нечётных элементов исходного списка.
✔ Нумерация начинается с единицы.
'''

lst = [1, 5, 7, 8, 4, 5, 12, 4, 5, 12, 4, 5, 86, 2, 45, 2]
new_lst = []
for i in range(len(lst)):
    if lst[i] % 2 != 0:
        new_lst.append(i+1)
print(new_lst)

print(f'Нечетные элементы в списке стоят на номерах: {[i + 1 for i in range(len(lst)) if lst[i] %2 != 0]}')
