'''
Проверка
'''

import logging

logging.basicConfig(
    filename="log/log.log",     # записывает в файл log.log в папке log
    encoding='utf-8',           # кодировка utf-8
    format='{asctime} {levelname} {funcName}->{lineno}: {msg}',
    # будет выдаваться сообщение типа:
    # время, название лога, имя функции -> номер строки: сообщение
    style='{',              # используется str.format
    level=logging.WARNING   # уровень выше warning (warning, error и critical)
    )
