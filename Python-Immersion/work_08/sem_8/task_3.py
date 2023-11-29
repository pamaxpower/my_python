'''
Задание №3

Напишите функцию, которая сохраняет созданный в
прошлом задании файл в формате CSV
'''
import json
import csv

def save_json_as_csv(json_file, csv_file):
    with open(json_file, 'r', encoding='utf-8') as f_json, \
        open(csv_file, 'w', newline='', encoding='utf-8') as f_write:
        data = json.load(f_json)
        res = []
        for key, values in data.items():
            for k1, v1 in values.items():
                res.append({
                    'level': key,
                    'user_id': k1,
                    'name': v1})

        writer = csv.DictWriter(f_write, \
                fieldnames=['level', 'user_id', 'name'], \
                dialect='excel', quoting=csv.QUOTE_NONNUMERIC, \
                delimiter=',')
        
        writer.writeheader()
        writer.writerows(res)

        print('Запись завершена')
        #print(data)
        # csv_write = csv.writer(f_write)

        # csv_write.writerow(data.keys())

        # for k,v in data.items():
        #     csv_write.writerow(v.items())


save_json_as_csv('list_name.json', 'list_name.csv')