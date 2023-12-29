'''
Действия при выходе из МК
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
        self.connection = sqlite3.connect(self.name)
        self.cursor = self.connection.cursor()
        return self.cursor
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        определяем действия при выходе из МК
        :param exc_type: тип ошибки
        :param exc_val: текст который хранится внутри ошибки
        :param exc_tb: текст трассировки (т.е. набора действия, приведших к ошибки
        """
        self.connection.commit()
        self.connection.close()
        self.cursor = self.connection = None


# экземпляр хранит имя базы, которое задается 1 раз
db = DB('sqlite_1.db')


with db as cur:
    cur.execute("""create table if not exists users(name, age);""")
    cur.execute("""insert into users values ('Гвидо', 66);""")