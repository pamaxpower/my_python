'''
Базовые регистраторы

Обычно в коде не используют прямое обращение через имя модуля,
в это мслучае использую функцию уровня модуля
logging.getLogger(name)

Правильный пример должен выглядеть так
'''

import logging

logging.basicConfig(level=logging.NOTSET)
logger = logging.getLogger(__name__)

logger.debug('Очень подробная отладочная информация. Заменяем множество "принтов"')
logger.info('Немного информации о работе кода')
logger.warning('Внимание! Надвигается буря!')
logger.error('Поймали ошибку. Дальше только неизвестность')
logger.critical('На этом всё')


