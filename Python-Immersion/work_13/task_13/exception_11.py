file = open('text.txt', 'r', encoding='utf-8')
try:
    data = file.read().split()
    print(data[len(data)])  # будет ошибка, тк длина списка 3, а макс.индекс 2
    # print(data[len(data)])  # код отработает без ошибка, выведет: "три"
finally:
    print('Закрываю файл')  # код сработает в любом случае
    file.close()
