"""
Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""
# with open(r"text2.txt", 'w', encoding='utf-8') as data:
#     while True:
#         line = input('Введите текст: \n')
#         if line == '':
#             break
#         data.write(line + '\n')


count_str = 0
with open("text2.txt", 'r', encoding='utf-8') as data:
    line = data.readlines()
    print(line)
    for i in range(len(line)):
        el = line[i].split()
        print(f'Количество слов в строке {i+1} равно: {len(el)}')
print(f'Количество строк в файле равно: {len(line)}')
