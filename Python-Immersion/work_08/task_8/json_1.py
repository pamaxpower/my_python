'''
JSON - Java Script Object Notation - формат текстовых данных

Преобразование JSON в Python
- из объекта json в виде отдельного текстового файла -> с помощью функции load() 
'''

import json

# Загружаем json-объект из файла и проводи его десериализацию

with open('user.json', 'r', encoding='utf-8') as f:
    json_file = json.load(f)

    
print(f'{type(json_file) = }\n{json_file = }')
print(f'{json_file["name"] = }')
print(f'{json_file["address"]["geo"] = }')
print(f'{json_file["email"] = }')
