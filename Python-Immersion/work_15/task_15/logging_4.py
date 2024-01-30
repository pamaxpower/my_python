import logging
from other import log_all

logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger('Основной файл проекта')
logger.warning('Внимание! Используем вызов функции из другого модуля')
log_all()

# не смотря на попытку использовать все уровни логирования, 
# срабатывают только предупреждения и выше. 
# Функция getLogger взяла конфигурацию basicConfig из 
# основного файла проекта.
