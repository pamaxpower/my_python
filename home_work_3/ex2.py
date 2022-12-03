"""
Реализовать функцию, принимающую несколько параметров, описывающих данные
пользователя:
имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
"""


def person(name, last_name, year, city, email, phone):
    """
    "Функция, собирающая данные о пользователе"
    :param name: "Имя"
    :param last_name: "Фамилия"
    :param year: "Год рождения"
    :param city: "Город проживания"
    :param email: "Электронная почта"
    :param phone: "Номер телефона"
    :return: Список данных о пользователе
    """
    my_list = [name, last_name, year, city, email, phone]
    return my_list


a = person(
    name=input('Имя: '),
    last_name=input('Фамилия: '),
    year=input('Год рождения: '),
    city=input('Город проживания: '),
    email=input('Электронный адрес: '),
    phone=input('Номер телефона: ')
)
print(a)
