# зарезервированные слова:
# while - начало цикла, 
# continue - возврат в начало цикла, 
# break - завершение цикла, 
# else - действие после цикла

num = float(input('Введите число: '))
count = 0
while count < num:
    print(count)
    count += 2
