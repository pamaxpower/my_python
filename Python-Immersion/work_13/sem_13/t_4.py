"""
Задание №5
📌 Доработаем задачи 3 и 4. Создайте класс проекта, который
имеет следующие методы:
📌 загрузка данных (функция из задания 4)
📌 вход в систему - требует указать имя и id пользователя. Для
проверки наличия пользователя в множестве используйте
магический метод проверки на равенство пользователей.
Если такого пользователя нет, вызывайте исключение
доступа. А если пользователь есть, получите его уровень из
множества пользователей.
📌 добавление пользователя. Если уровень пользователя
меньше, чем ваш уровень, вызывайте исключение уровня
доступа.
"""

from json import dump, load
import os

class BaseError(Exception):
    pass


class LevelError(BaseError):
    def __init__(self, message="Ошибка уровня"):
        self.message = message
        # super().__init__(self.message)


class AccessError(BaseError):
    """Исключение, связанное с ошибкой доступа."""
    def __init__(self, message="Ошибка доступа"):
        self.message = message
        # super().__init__(self.message)


def create_users_from_json(file_path):
    users = list()

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = load(file)
            for identifier, user_data in data.items():
                users.append(User(name=user_data["имя"], identifier=identifier, access_level=user_data["уровень_доступа"]))
    except FileNotFoundError:
        print(f"Файл {file_path} не найден.")
    except IOError as e:
        print(f"Произошла ошибка при чтении файла: {e}")

    return users


def save_to_json(name, identifier, access_level):

    file_path = "data.json"

    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as file:
            data = load(file)
    else:
        data = {}

    data[identifier] = {
        "имя": name,
        "уровень_доступа": access_level
    }

    with open(file_path, "w", encoding="utf-8") as file:
        dump(data, file, ensure_ascii=False, indent=2)


class User:
    def __init__(self, name, identifier, access_level):
        self.name = name
        self.identifier = identifier
        self.access_level = access_level

    def __repr__(self):
        return f"User(name='{self.name}', identifier='{self.identifier}', access_level={self.access_level})"

    def __eq__(self, other):
        if isinstance(other, User):
            return self.identifier == other.identifier
        return False


class Project:
    def __init__(self):
        self.users = list()

    def load_data(self, file_path):
        self.users = create_users_from_json(file_path)

    def login(self, identifier):
        res = {user.identifier: user.access_level for user in self.users}
        try:
            if identifier in res:
                print('Пользователь найден')
                return res[identifier]
            raise AccessError("Пользователь не найден или доступ запрещен.")
        except AccessError as error:
            return error

    def add_user(self, new_user, current_user_level):
        try:
            if new_user.access_level > current_user_level:
                raise LevelError("Ваш уровень доступа слишком низкий для добавления этого пользователя.")
        except LevelError as error:
            print(error)
        else:
            # self.users.append(new_user)
            save_to_json(new_user.name, new_user.identifier, new_user.access_level)


user_1 = User('Виктор', '456', 5)
my_p = Project()
my_p.load_data('data.json')
print(my_p.users)
print(my_p.login('Виктор', '777'))
my_p.add_user(user_1, 7)
print(my_p.login('456'))


# def get_login_level(name):

#         try:
#             for el in CheckUserLogin.users:
#                 if name == el.name:
#                     return 'Пользователь найден'
#                 raise NameErr()
#         except NameErr as e:
#             print(e)
