'''
Запись в csv

- для записи используют функцию writer()? которая на вход 
принимает файловый дискриптор и доп.параметры записи.
- данные не записываются в файл, пока у возвращенного объекта 
не будет вызвана функция writerow() для записи одной строки
(или writerows() для записи нескольких строк)


'''
import csv

# с помощью менеджера контекстов открываем два файла: 
# первый для чтения, второй - для записи
with (
    open('biostats.csv', 'r', newline='') as f_read,
    open('new_biostats.csv', 'w', newline='', encoding='utf-8') as f_write
):
    # возвращает объект для чтения
    csv_read = csv.reader(f_read, quoting=csv.QUOTE_NONNUMERIC)
    # возвращаем объект для записи
    # dialect='excel' - объект экселя
    # delimiter='' - разделитель для записи по пробелу
    # quotechar='|' - если в ячейке есть пробел, то всю ячейку экранируем |
    # quoting=csv.QUOTE_MINIMAL - символ экранировки используем по минимуму
    csv_write = csv.writer(f_write, dialect='excel', delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    
    all_data = []
    
    # в цикле обходим все строки файла
    for i, line in enumerate(csv_read):
        # строку с заголовком (первую по счету) записываем методом writerow()
        if i == 0:
            csv_write.writerow(line)
        # для остальных строк увеличиваем возраст на 1 и преобразуем вещественные числа в целые
        else:
            # print(line)
            line[2] += 1
            for j in range(2, 4 + 1):
                line[j] = int(line[j])
            # все сохраняем в матрицу
            all_data.append(line)
    # сохраняем матрицу в файл
    csv_write.writerows(all_data)