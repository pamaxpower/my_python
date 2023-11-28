'''
CSV (Comma-Separated Values)
- значения, разделенные запятыми
- текстовый формат, предназначенный для представления табличных данных
- используют для выгрузки из БД и электронных таблиц для анализа данных


* Чтение CSV

'''

import csv
with open('biostats.csv', 'r', newline='') as f:
    csv_file = csv.reader(f)
    for line in csv_file:
        print(line)

    print(type(line))
