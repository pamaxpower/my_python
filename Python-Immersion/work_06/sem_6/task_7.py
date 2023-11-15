'''
Задание №7
� Создайте модуль и напишите в нём функцию, которая
получает на вход дату в формате DD.MM.YYYY
� Функция возвращает истину, если дата может существовать
или ложь, если такая дата невозможна.
� Для простоты договоримся, что год может быть в диапазоне
[1, 9999].
� Весь период (1 января 1 года - 31 декабря 9999 года)
действует Григорианский календарь.
� Проверку года на високосность вынести в отдельную
защищённую функцию.
'''

def leap_year(num):
    if num % 4 == 0 and (num % 100 != 0 or num % 400 == 0):
        # print('Год високосный')
        return True
    else:
        return False

def func(date):
    day, month, year = map(int, date.split('.'))

    if month > 12:
        flag = False
    elif month in [1,3,5,7,8,10,12] and day > 31:
        flag = False
    elif month in [4,6,9,11] and day > 30:
        flag = False
    
    elif leap_year(year):
        if month == 2 and day > 29:
            flag = False
        else:
            flag = True
    else:
        if month == 2 and day > 28:
            flag = False
        else:
            flag = True

    return flag
    # if flag:
    #     print('Такая дата существует')
    # else: 
    #     print('Такой даты не существует')

print(func('29.2.2000'))


# def func1(date):

#     day, month, year = map(int, date.split('.'))
#     if year in range(1000, 2024) and month in range(1, 13) and day in range(1, 32):
#         if year % 400 == 0 and month == 2 or year % 4 == 0 and year % 100 != 0 and month == 2:
#             if day in range(1, 30):
#                 return True
#             else:
#                 return False
#         if month in [1, 3, 5, 7, 8, 10, 12]:
#             return True
#         elif month == 2:
#             if day in range(1, 29):
#                 return True
#             else:
#                 return False
#         else:
#             if day in range(1, 31):
#                 return True
#             else:
#                 return False
#     else:
#         return False
    
# print(func1('29.2.2000'))