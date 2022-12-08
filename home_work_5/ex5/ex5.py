"""
Создать (программно) текстовый файл, записать в него программно набор чисел, h
азделенных пробелами.

Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

with open('text5.txt', 'w', encoding='utf-8') as data:
    line = input('Введите цифры через пробел \n')
    data.writelines(line)
    numbers = []
    
    for el in line.split():
        numbers.append(int(el))

    print(f'Сумма числе в файле равна: {sum(numbers)}')