'''
Проверка
'''

import csv 

with open('quest.csv', 'w', newline='', encoding='utf-8') as f_write:
    csv_write = csv.DictWriter(f_write, \
        fieldnames=["number", "name", "data"], restval='Hello world!', \
        dialect='excel', delimiter='#', quotechar='=', \
        quoting=csv.QUOTE_NONNUMERIC)

    csv_write.writeheader()
    dict_row = {}
    for i in range(10):
        dict_row['number'] = i
        dict_row['name'] = str(i)
        csv_write.writerow(dict_row)

# записываем файл quest.csv в котором заголовок будет по названию
# полей fieldnames (number, name, data) - имена столбцов
# записываем словарь dict_row: 
# ключ number - порядковое число от 0 до 9 вкл, 
# ключ name - строковое значение числа
# все записываем файл в столбце data будет значение 'Hello world!'
# разделители между ячейками символ #
# обрамление строк символом = (вместо кавычек)

