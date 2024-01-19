import json

class User:
    """Класс пользователя"""
    def __init__(self, name, user_id, level) -> None:
        self.name = name
        self.user_id = user_id
        self.level = level

    def __str__(self):
        return f'User:{self.name}, id:{self.user_id},  level:{self.level}'


def func():
    res = []
    my_dict = {}
    list_id = []
    while True:
        user_id = int(input('Введите ваш личный идентификатор: '))
        if user_id in list_id:
            print('такой id уже есть')
            continue
        list_id.append(user_id)

        name = input('Введите ваше имя: ')
        access_level = int(input('Введите уровень доступа (от 1 до 7): '))
        
        if access_level in my_dict:
            my_dict[access_level][user_id] = name
        else:
            my_dict[access_level] = {user_id: name}
        res.append(my_dict)

        stop_input = input("Хотите закончить ввод? (y/n): ")
        if stop_input.lower() in ['y', 'н', 'yes', 'да']:
            with open('list_name.json', 'w', encoding='utf-8') as f:
                json.dump(my_dict, f, separators=(',\n', ' : '), ensure_ascii=False)
        
            break

# func()

user_group = set()

def load_users(path):
    """Метод загрузки данных из файла"""
    with open(path, 'r', encoding='UTF-8') as js_f:
        user_dict = json.load(js_f)
        for level, user_list in user_dict.items():
            for id, name in user_list.items():
                user_group.add(User(name, id, level))

if __name__ == '__main__':
    
    load_users('list_name.json')

    for el in user_group:
        print(el)