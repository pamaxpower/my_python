'''
Работа менеджера контекста сразу с несколькими файлами
'''
# для версии Python 3.7,8,9

# with open('text_data.txt', 'r+', encoding='utf-8') as f1, \
#         open('bin_data', 'rb') as f2, \
#         open('data.txt', 'r', encoding='utf-8', errors='backslashreplace') as f3:
    
#     print(list(f1))
#     print(list(f2))
#     print(list(f3))

# для переноса строк используется символ \


# для версии Python 3.10 можно использовать круглые скобки 

with (
    open('text_data.txt', 'r+', encoding='utf-8') as f1,
    open('bin_data', 'rb') as f2,
    open('data.txt', 'r', encoding='utf-8', errors='backslashreplace') as f3
    ):
    print(list(f1))
    print(list(f2))
    print(list(f3))
