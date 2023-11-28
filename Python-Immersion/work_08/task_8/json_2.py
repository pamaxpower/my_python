'''
Преобразование JSON в Python

- из многострочного str в Python
-> loads() - функция для загрузки строк

'''

import json

# есть информация в виде многострочного str в py-файле
json_text = """
[
    {
        "userId": 1,
        "id": 9,
        "title": "nesciunt iure omnis dolorem tempora et accusantium",
        "body": "consectetur animi nesciunt iure dolore"
    },
    {
        "userId": 1,
        "id": 10,
        "title": "optio molestias id quia eum",
        "body": "quo et expedita modi cum officia vel magni"
    },
    {
        "userId": 2,
        "id": 11,
        "title": "et ea vero quia laudantium autem",
        "body": "delectus reiciendis molestiae occaecati non minima eveniet qui voluptatibus"
    },
    {
        "userId": 2,
        "id": 12,
        "title": "in quibusdam tempore odit est dolorem",
        "body": "praesentium quia et ea odit et ea voluptas et"
    }
]"""

# нужно превратить его из json строки в объекты python

# выводим информация о файле и смотрим, что в нем содержится
print(f'{type(json_text) = }\n{json_text = }')

# функция loads() принимает строку, как структуру json и преобразует ее к нужным типа python
json_list = json.loads(json_text)

# получаем список list с 4 словарями dict внутри 
print(f'{type(json_list) = }\t{len(json_list) = }\n{json_list =}')
