'''
Математика с датами

'''

from datetime import datetime, timedelta

# разница во времени
date_1 = datetime(2012, 12, 21)
date_2 = datetime(2017, 8, 19)
delta = date_2 - date_1

print(f'{delta = }\t-\t{delta}')

# дата 33-летия
birthday = datetime(1503, 12, 14)
dlt = timedelta(days=365.25 * 33)
new_date = birthday + dlt

print(f'{new_date = }\t-\t{new_date}')
