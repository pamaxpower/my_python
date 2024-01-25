"""
Запуск тестов с командной строки
(например в терминале powershell)

PS C:\Users\PycharmProjects> python -m doctest .\prime.py
PS C:\Users\PycharmProjects> python -m doctest .\prime.py -v
PS C:\Users\PycharmProjects> python -m doctest .\prime.md
PS C:\Users\PycharmProjects> python -m doctest .\prime.md -v

PS C:\Users\PycharmProjects> -> папка интерпретатора
python -m - интерпретатор
doctest - вызываем модуль
.\prime.py - путь до файла, который надо тестировать

если у файла расширение .py - запустится функция testmod(), 
если расширение будет другое - функция testfile()

ключ -v включает режим подробного вывода результатов тестирования
"""


