'''
Задание №4

Прочитайте созданный в прошлом задании csv файл без
использования csv.DictReader.

Дополните id до 10 цифр незначащими нулями.

В именах первую букву сделайте прописной.

Добавьте поле хеш на основе имени и идентификатора.

Получившиеся записи сохраните в json файл, 
где каждая строка csv файла представлена как отдельный 
json словарь.

Имя исходного и конечного файлов передавайте как аргументы
функции.
'''

from csv import DictReader
from json import dump

with open('list_name.csv', 'r', encoding='utf-8', newline='') as f, \
        open('new_list.json', 'w', encoding='utf-8') as new_file:
    
    csv_file = DictReader(f, fieldnames=['level', 'user_id', 'name', 'hash'], \
        # restkey='new', \
        restval=' - ')
    
    
    res = []
    for i, line in enumerate(csv_file):
        if i == 0:
            continue
        my_dict = {}
        
        level, user_id, name, *_ = line.values()
        my_dict['level'] = int(level)
        my_dict['user_id'] = user_id.zfill(10)
        my_dict['hash'] = hash(user_id)
        my_dict['name'] = name.title()
            
        res.append(my_dict)

    dump(res, new_file, indent=2, separators=(',', ':'), ensure_ascii=False)
    # res = []
    # for i, line in enumerate(csv_file):
    #     print(line)
    #     if i != 0:
    #         line[1] = line[1].zfill(10)
    #         line[2] = line[2].capitalize()
    #         line.append(hash())
    #     res.append(line)
    # print(res)

