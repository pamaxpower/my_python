'''
Задание №6

Напишите функцию, которая преобразует pickle файл
хранящий список словарей в табличный csv файл.

Для тестированию возьмите pickle версию файла из задачи
4 этого семинара.

Функция должна извлекать ключи словаря для заголовков
столбца из переданного файла.
'''
from pickle import load
from csv import DictWriter, QUOTE_NONNUMERIC


def save_pickle_as_csv(pickle_file, csv_file):

    with open(pickle_file, 'rb') as f, \
            open(csv_file, 'w', encoding='utf-8', newline='') as csv_f:
        res = load(f)

        my_write = DictWriter(csv_f, delimiter=',', \
            fieldnames=['level', 'user_id', 'name', 'hash'], \
            dialect='excel', quoting=QUOTE_NONNUMERIC)
        my_write.writeheader()
        my_write.writerows(res)



save_pickle_as_csv('new_list.pickle', 'new_8.csv')