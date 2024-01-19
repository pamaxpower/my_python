'''
Задание №2

Напишите функцию, которая в бесконечном цикле запрашивает 
имя, личный идентификатор и уровень доступа (от 1 до 7).

После каждого ввода добавляйте новую информацию в
JSON файл.

Пользователи группируются по уровню доступа.

Идентификатор пользователя выступает ключём для имени.

Убедитесь, что все идентификаторы уникальны независимо
от уровня доступа.

При перезапуске функции уже записанные в файл данные
должны сохраняться.

'''
import json

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
        # my_dict['id'] = id
        # my_dict['name'] = name
        # my_dict['level'] = access_level
        res.append(my_dict)

        stop_input = input("Хотите закончить ввод? (y/n): ")
        if stop_input.lower() in ['y', 'н', 'yes', 'да']:
            with open('list_name.json', 'a', encoding='utf-8') as f:
                json.dump(my_dict, f, separators=(',\n', ' : '), ensure_ascii=False)
        
            break

# в классе
# def func():
#     res = []
#     while True:
#         user_id = int(input('Введите ваш личный идентификатор: '))
        
#         name = input('Введите ваше имя: ')
#         access_level = int(input('Введите уровень доступа (от 1 до 7): '))
#         my_dict = {
#                 'id': user_id, 
#                 'name': name, 
#                 'level': access_level,
#                 }
#         res.append(my_dict)    
     
#         if input('Выход: ').lower() in ['y', 'yes', 'da', 'н', 'да']:
#             with open('list_name.json', 'w', encoding='utf-8') as f:
#                 json.dump(res, f, separators=(',\n', ':'), ensure_ascii=False)
#             break

# мое 
    # my_dict = {}
    # list_id = []
    # while True:
    #     iid = int(input('Введите ваш личный идентификатор: '))
    #     if iid in list_id:
    #         print('такой id уже есть')
    #         continue
    #     list_id.append(iid)

    #     name = input('Введите ваше имя: ')
    #     level = int(input('Введите уровень доступа (от 1 до 7): '))
        
    #     if level in my_dict:
    #         my_dict[level][iid] = name
    #     else:
    #         my_dict[level] = {iid: name}