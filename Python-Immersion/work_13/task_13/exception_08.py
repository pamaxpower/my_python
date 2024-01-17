'''
команда else
- используется если надо выполнить код, только в случае успешного завершения блока try

Однако, блок else не сработает если внутри try будет:
- вызвано исключение
- выполнена команда return
- выполнена команда break
- выполнена команда continue

'''

MAX_COUNT = 5
result = None
for count in range(1, MAX_COUNT + 1):
    try:
        num = int(input('Введите целое число: '))
        print('Успешно получили целое число')
    except ValueError as e:
        print(f'Попытка {count} из {MAX_COUNT} завершилась ошибкой {e}')
    else:
        result = 100 / num
        break

print(f'{result = }')
