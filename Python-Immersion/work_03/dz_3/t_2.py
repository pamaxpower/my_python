'''
В большой текстовой строке text подсчитать количество 
встречаемых слов и вернуть 10 самых частых. 
Не учитывать знаки препинания и регистр символов.

Слова разделяются пробелами. Такие слова как don t, it s, didn t 
итд (после того, как убрали знак препинания апостроф) считать 
двумя словами.
Цифры за слова не считаем.

Отсортируйте по убыванию значения количества повторяющихся слов.
'''

import re

text = "Installing Python is generally easy, and nowadays many Linux and UNIX distributions include a recent Python. Even some Windows computers (notably those from HP) now come with Python already installed. If you do need to install Python and arent confident about the task you can find a few notes on the BeginnersGuide/Download wiki page, but installation is unremarkable on most platforms."

# Удаляем знаки препинания и цифры
text_modified = re.sub("[^A-Za-z]", " ", text)

# Разбиваем текст на слова и считаем их количество
_dict = {}
for el in text_modified.lower().split():
    _dict[el] = _dict.get(el, 0) + 1

# Сортируем словарь посредством формирования списка (ключ, значение)
_list = []
for key, value in _dict.items():
    _list.append((key, value))
    _list.sort(key=lambda x: x[1], reverse=True)

# Печатаем первые 10 самых используемых слов
print(_list[0:10])