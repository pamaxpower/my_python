"""Модуль modules"""

import subprocess
import chardet      # позволяет принять байты и получить исходную кодировку
import os

ARGS = ['ping', 'yandex.ru']
YA_PING = subprocess.Popen(ARGS, stdout=subprocess.PIPE)
print(YA_PING.stdout)
for line in YA_PING.stdout:
    # print(line)     # получаем байты. Латинница и цифры остаются как есть,
    # а кириллица переводится. Но оба остаюются типом bytes
    # print(line.decode('cp866'))     # расшифровка для виндовс

    result = chardet.detect(line)   # функция detect сканирует наш объект и
                                    # распознает  его кодировку
    #print(result)

    line = line.decode(result['encoding']) # декодируем строку в нужный нам формат
    print(line)

    #line = line.decode(result['encoding']).encode('utf-8')
    #print(line.decode('utf-8'))

print(os.name)