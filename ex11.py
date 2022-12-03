
my_list = [9, 7, 5, 5, 5, 3, 3, 2, 1]
rating = int(input('Введите элемент рейтинга: '))
for i in range(len(my_list)):
    if my_list[i] == rating:
        my_list.insert(i, rating)
print(my_list)