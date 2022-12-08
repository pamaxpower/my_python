"""Менеджеры контекста"""

with open("mtsuri.txt", encoding='utf-8') as f_obj:
    for line in f_obj:
        print(line)

# было
# f_obj = open("text.txt")

# стало
# with open("text.txt") as f_obj:
