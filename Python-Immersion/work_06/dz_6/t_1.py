'''
Вы работаете над разработкой программы для проверки корректности даты, 
введенной пользователем. На вход будет подаваться дата в формате "день.месяц.год". 
Ваша задача - создать программу, которая проверяет, является ли введенная дата корректной или нет.

Ваша программа должна предоставить ответ "True" (дата корректна) или "False" (дата некорректна) в зависимости от результата проверки.

Пример использования На входе:
date_to_prove = 15.4.2023

На выходе:
True
'''
def func(date):
    day, month, year = map(int, date.split('.'))
    if year in range(1000, 10000) and month in range(1, 13) and day in range(1, 32):
        if year % 400 == 0 and month == 2 or year % 4 == 0 and year % 100 != 0 and month == 2:
            if day in range(1, 30):
                return True
            else:
                return False
        if month in [1, 3, 5, 7, 8, 10, 12]:
            return True
        elif month == 2:
            if day in range(1, 29):
                return True
            else:
                return False
        else:
            if day in range(1, 31):
                return True
            else:
                return False
    else:
        return False
    
# date_to_prove = '15.4.2023'   # True
# date_to_prove = '0.5.2022'    # False
# date_to_prove = '12.0.2022'   # False
# date_to_prove = '12.5.-2022'  # False
# date_to_prove = '29.2.2020'   # True
# date_to_prove = '12.5.2022'   # True
# date_to_prove = '28.2.2021'   # True
date_to_prove = '31.12.9999'  # True 
# date_to_prove = '32.5.2022'   # False
# date_to_prove = '12.13.2022'  # False
# date_to_prove = '29.2.2021'   # False
# date_to_prove = '30.2.2020'   # False



print(func(date_to_prove))
    
