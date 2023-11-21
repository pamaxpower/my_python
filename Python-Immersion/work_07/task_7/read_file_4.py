'''
Чтение файла

4) for line in f: - через цикл for
- построчно считывает текст
'''

with open('text_data.txt', 'r', encoding='utf-8') as f:
    for line in f:
        print(line, end='')


# SIZE = 20
# with open('text_data.txt', 'r', encoding='utf-8') as f:
#     for line in f:
#         print(line[:-1])
#         # print(line.replace('\n', ''))