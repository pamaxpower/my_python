'''
Getter
- метод, выдающий себя за свойство - позволяют прочитать, 
но блокируют возможность записи

'''
class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def full_name(self):
        """
        не метод, а свойство
        :return: возвращает полное имя
        """
        return f'{self.first_name} {self.last_name}'

user = User('Стивен', 'Спилберг')
print(f'{user.first_name = }\n{user.last_name = }\n{user.full_name = }')

# user.full_name = 'Стивен Хокинг' # AttributeError: can't set attribute 'full_name'
user.last_name = 'Хокинг'
print(f'{user.first_name = }\n{user.last_name = }\n{user.full_name = }')
