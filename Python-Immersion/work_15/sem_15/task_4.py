'''
Задание №4

Функция получает на вход текст вида: “1-й четверг ноября”, “3-
я среда мая” и т.п.

Преобразуйте его в дату в текущем году.
Логируйте ошибки, если текст не соответсвует формату.

'''

import logging
from datetime import datetime, timedelta

logging.basicConfig(
    filename='log/t_4.log',
    filemode='a',
    format='{asctime} {levelname} функция "{funcName}()" строка {lineno}: {msg}',
    style='{',
    encoding='utf-8',
    level=logging.ERROR
)


def date_text(text):
    months = {'января': 1, 'февраля': 2, 'марта': 3, 'апреля': 4,
              'мая': 5, 'июня': 6, 'июля': 7, 'августа': 8,
              'сентября': 9, 'октября': 10, 'ноября': 11, 'декабря': 12}
    weekdays = {'понедельник': 0, 'вторник': 1, 'среда': 2, 'четверг': 3,
                'пятница': 4, 'суббота': 5, 'воскресение': 6}
    try:
        parts = text.split()
        if len(parts) != 3:
            raise ValueError('Не тот формат')
        week_number = int(parts[0][:-2])  # отбрасываем -й, -я
        day_of_week = weekdays[parts[1]]
        month_ = months[parts[2]]
        year_ = datetime.now().year

        first_day = datetime(year_, month_, 1)  # первый день года
        # print(first_day.weekday())            # день недели (по счету)

        # считаем число дня недели
        requested_day = first_day + timedelta(
            days=(day_of_week - first_day.weekday() + 7) % 7)
        # first_day - первый день года
        # timedelta(days=(day_of_week - first_day.weekday() + 7) % 7)

        text_date = requested_day + timedelta(weeks=week_number - 1)

        return text_date.date()

    except Exception as e:
        logging.error(f'Ошибка {e}')

if __name__ == '__main__':
    print(date_text('3-я суббота января fg'))
