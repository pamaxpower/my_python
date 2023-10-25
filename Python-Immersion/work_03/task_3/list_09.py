'''
Проверка. Пример
'''

lst = [2, 4, 6, 2, 8, 10, 12, 14, 16, 18]

print(lst[2:6:2])               # [6:8]
print(lst.pop())                # 18
print(lst.extend([314, 42]))     # None
print(lst.sort(reverse=False))  # None
print(lst)                      # [2, 2, 4, 6, 8, 10, 12, 14, 16, 42, 314]
