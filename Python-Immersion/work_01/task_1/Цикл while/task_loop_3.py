min_limit = 0
max_limit = 10
while True:             # бесконечнй цикл
    print(f'Введи число между {min_limit} и {max_limit}: ')
    num = float(input())
    if num < min_limit or num > max_limit:
        print('Неверно')
    else:
        break
print(f'Вы ввели число: {num}')
