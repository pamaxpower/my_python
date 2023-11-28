'''
Проверка
'''

import pickle

my_dict = {'numbers': [42, 4.1415, (7 + 3j)], 
            'functions': (sum, max),
            'others': {False, True, 'Hello world!'}
            }

# словарь сохранится в строку байт
res = pickle.dumps(my_dict)

# открываем файл байт для записи
with open('quest.pickle', 'wb') as f:
    # в открытый файл будет записана строка байт 
    # (которая имеет строковый вид)
    pickle.dump(f'{res = }', f)

# т.е. по сути, будет проведена двойная сериализация
