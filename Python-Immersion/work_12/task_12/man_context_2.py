'''
Действия при входе в менеджер контекста (МК)
'''

import sqlite3

class DB:
    def __init__(self, name):
        self.name = name
        self.connection = None
        self.cursor = None

    
    def __enter__(self):
        """
        определяем действия при входе в МК
        """
        # установлениен соединения с базой
        self.connection = sqlite3.connect(self.name)
        # получение курсора
        self.cursor = self.connection.cursor()
        return self.cursor

# экземпляр хранит имя базы, которое задается 1 раз
db = DB('sqlite_1.db')


#при работе с МК получаем ошибку отстутствия выхода из МК
with db as cur:     # AttributeError: __exit__
    cur.execute("""create table if not exists users(name, age);""")
    cur.execute("""insert into users values ('Гвидо', 66);""")
