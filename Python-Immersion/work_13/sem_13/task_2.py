'''
Задание №2

Создайте функцию аналог get для словаря.
Помимо самого словаря функция принимает ключ и
значение по умолчанию.
При обращении к несуществующему ключу функция должна
возвращать дефолтное значение.
Реализуйте работу через обработку исключений.

'''

def get_dict(m_dict, key, default=None):
    try:
        return m_dict[key]
    except KeyError:
        return default
    
my_dict = {'a': 1, 'b': 2}
print(get_dict(my_dict, 'a', 'Пусто'))
print(get_dict(my_dict, 'd', 'Пусто'))