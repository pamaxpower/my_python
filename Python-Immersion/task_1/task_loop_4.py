min_limit = 0
max_limit = 10
count = 3
num = None

while count > 0:
    print(f'Осталось {count} попыток')
    count -= 1

    print(f'Введи число между {min_limit} и {max_limit}: ')
    num = float(input())
    if num < min_limit or num > max_limit:
        print('Неверно')
    else:
        break

else:
    print('Попытки закончились. Сожалею')
    quit()

print(f'Вы ввели число: {num}')
