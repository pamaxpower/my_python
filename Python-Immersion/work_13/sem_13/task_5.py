'''
Задание №5

Доработаем задачи 3 и 4. Создайте класс проекта, который
имеет следующие методы:

загрузка данных (функция из задания 4)

вход в систему - требует указать имя и id пользователя. Для
проверки наличия пользователя в множестве используйте
магический метод проверки на равенство пользователей.

Если такого пользователя нет, вызывайте исключение
доступа. А если пользователь есть, получите его уровень из
множества пользователей.

добавление пользователя. Если уровень пользователя
меньше, чем ваш уровень, вызывайте исключение уровня
доступа.
'''
from task_3 import AccessError, LevelError
import json


class User:
    def __init__(self, name: str, user_id: str, level: str = '0') -> None:
        self.name = name
        self.user_id = user_id
        self.level = level

    def __str__(self):
        return f'User:{self.name}, id:{self.user_id},  level:{self.level}'

    # def __eq__(self, other):
    #     if isinstance(self, other):
    #         return self.user_id == other.user_id
    #     return False


class Project:
    def __init__(self):
        self.user_group = set()


    def load_users(self):
        """Метод загрузки данных из файла"""
        with open('list_name.json', 'r', encoding='UTF-8') as js_f:
            user_dict = json.load(js_f)
        for level, user_list in user_dict.items():
            for u_id, name in user_list.items():
                self.user_group.add(User(name, u_id, level))


    def enter_system(self, name, user_id):
        user_check = User(name, user_id, level=None)
        print(user_check)
        try:
            for el in self.user_group:
                if name == el.name and user_id == int(el.user_id):
                    print('Такой пользователь есть')
                    return el
            raise AccessError('')
        except AccessError:
            print('Такого пользователя нет')

        # for el in self.user_group:
        #     if name == el.name:
        #         print('Такой пользователь есть')
        #         return el
        # raise AccessError('Пользователь не найден')
            add = input('Добавить пользователя с таким именем? y/n: ')
        
            if add.lower() in ['y', 'н', 'yes', 'да']:
                n_lev = int(input('Введите уровень пользователя: '))
            n_us = User(name, user_id, n_lev)
            self.user_group.add(n_us)
            return f'Пользователь {n_us} успешно добавлен'
            

    def add_user(self, name, uid, ul):
        current_level = 3
        if ul < current_level:
            raise LevelError('Ошибка уровня')
        else:
            self.user_group.add(User(name, uid, ul))
        

if __name__ == "__main__":
    a = Project()
    a.load_users()

    # print(*a.user_group, sep='\n')        # вывод списка пользователей в проекте a
    
    # u1 = User('sdhfwty', 13564, 5)        # новый пользователь
    # a.add_user('sdhfwty', 13564, 5)       # добавляем нового пользователя в проект a
    # print(*a.user_group, sep='\n')

    # print(a.enter_system('ust', 216))     # пробуем залогиниться - пользователь есть -> получаем данные
    # print(a.enter_system('ust', 47387))   # пробуем залогиниться - пользователя нет (ошибка id)
    # print(a.enter_system('hgjk', 1235))   # пробуем залогиниться - пользователя нет (ошибка в имени)
    print(*a.user_group, sep='\n')




