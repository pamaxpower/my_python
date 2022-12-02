'''
Списки

'''
list1 = [1,2,3,4,5]
list2 = list1

for e in list1:
    print(e, end =' ')
print()
for e in list2:
    print(e, end = ' ')
print()

list1[0] = 123          # Когда мы поменяет значение в 1 списке, оно автоматически меняется и во 2
list2[1] = 333          # Если поменять значение во 2 списке, оно изменится и в первом
                        # объясняется это тем, что обе переменные ссылаются на одну и ту же область памяти, по сути они являются лишь ссылками

for e in list1:
    print(e, end =' ')
print()
for e in list2:
    print(e, end = ' ')

print()
print(list1.pop(2))             # удаляет элемент и показывает удаленный его значение
print(list1.insert(3, 11))      # добавляет значение 11 на позицию 3-его элемента
print(list1)
