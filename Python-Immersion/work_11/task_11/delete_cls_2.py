'''
Удаление экземпляров класса, метод del()

- зарезервированное слово del не удаляет объекты, онр разрывает
связь между переменной и объектом, на который указывает переменная 
- после вызова del у объекта уменьшается счетчик ссылок

'''

import sys

class User:
    def __init__(self, name: str):
        self.name = name
        
        print(f'Создал {self.name = }')
    def __del__(self):
        print(f'Удаление экземпляра {self.name}')


u_1 = User('Спенглер')
print(sys.getrefcount(u_1)) # считаем кол-во ссылок и видим число 2
                            # 1 ссылка на объект + 1 ссылка от вызова метода getrefcount()

u_2 = u_1                   # копия экземпляра
print(sys.getrefcount(u_1), sys.getrefcount(u_2))

del u_1                     
print(sys.getrefcount(u_2))
print('Завершение работы')
