'''
Задание №1

Вспоминаем задачу 3 из прошлого семинара. 
Мы сформировали текстовый файл с псевдо именами и 
произведением чисел.

Напишите функцию, которая создаёт из созданного ранее
файла новый с данными в формате JSON.

Имена пишите с большой буквы.

Каждую пару сохраняйте с новой строки.
'''
import json

def save_txt_as_json(txt, json_f):
    with open(txt, 'r', encoding='utf-8') as f_txt, \
            open (json_f, 'w', encoding='utf-8') as f_json:
        line = f_txt.readlines()
        my_dict = {}
        for el in line:
            k, v = el.split('-')
            my_dict[k.title()] = float(v)
        json.dump(my_dict, f_json, indent=2, separators=(',\n', ':'), ensure_ascii=False)


txt_file = 'task_3_copy.txt'
json_file = 'task_1.json'
save_txt_as_json(txt_file, json_file)