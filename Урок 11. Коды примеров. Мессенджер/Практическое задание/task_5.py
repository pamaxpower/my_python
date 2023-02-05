"""
Задание 5.

Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
преобразовать результаты из байтовового в строковый тип на кириллице.

Подсказки:
--- используйте модуль chardet, иначе задание не засчитается!!!
"""

# пример с yandex.ru был на семинаре, поэтому заменил на vc.com
import subprocess
import chardet  # позволяет принять байты и получить исходную кодировку

arg1 = ['ping', 'youtube.com']
arg2 = ['ping', 'vk.com']

yt_ping = subprocess.Popen(arg2, stdout=subprocess.PIPE)
print(yt_ping.stdout)
for line in yt_ping.stdout:
    result = chardet.detect(line)  # функция detect сканирует наш объект
    # print(result)      # возвращает словарь, где указана кодировка
    line = line.decode(
        result['encoding'])  # декодируем строку в нужный нам формат
    print(line)

vc_ping = subprocess.Popen(arg1, stdout=subprocess.PIPE)
print(vc_ping.stdout)
for line in vc_ping.stdout:
    result = chardet.detect(line)
    line = line.decode(result['encoding'])
    print(line)
