'''
Задача 1

Напишите функцию группового переименования файлов в папке test_folder под названием rename_files. Она должна:

a. принимать параметр желаемое конечное имя файлов. 
При переименовании в конце имени добавляется порядковый 
номер. (desired_name)

b. принимать параметр количество цифр в порядковом номере.
(num_digits)

c. принимать параметр расширение исходного файла. 
Переименование должно работать только для этих файлов 
внутри каталога. (source_ext)

d. принимать параметр расширение конечного файла.
(target_ext)

e. принимать диапазон сохраняемого оригинального имени. 
Например для диапазона [3, 6] берутся буквы с 3 по 6 из 
исходного имени файла. К ним прибавляется желаемое 
конечное имя, если оно передано. Далее счётчик файлов и 
расширение.

f. Папка test_folder доступна из текущей директории
'''
import os
import shutil
from t_1_ans import rename_files_2

# Создать тестовую папку
folder_name = "test_folder"
folder_path = os.path.join(os.getcwd(), folder_name)
if os.path.exists(folder_path):
    shutil.rmtree(folder_path)
os.makedirs(folder_path)


# Заполнить тестовую папку
for i in range(10):
    file_name = f"test{i}.txt"
    file_path = os.path.join(folder_path, file_name)
    with open(file_path, "w") as file:
        file.write("This is a test file.\n")
        file.close()

file_name = "test.doc"
file_path = os.path.join(folder_path, file_name)

with open(file_path, "w") as file:
    file.write("This is a test file.\n")
    file.close()



def rename_files(desired_name, num_digits, source_ext, target_ext, name_range=None):
        # Путь к папке test_folder
    folder_path = "test_folder"
        # Получаем список файлов в папке test_folder
    files = os.listdir(folder_path)
        # Перебираем каждый файл
    for i, file_name in enumerate(files):
            
            # Проверяем расширение файла
        if file_name.endswith(source_ext):
                
                # Генерируем новое имя файла
            new_name = desired_name
                
                # Добавляем оригинальное имя согласно диапазону
            if name_range is not None:
                start = name_range[0] - 1 # Так как индексация начинается с 0
                end = name_range[1]
                original_name = file_name[start:end]
                new_name += original_name
                
                # Заполняем номер нулями до заданной длины
            num = str(i).zfill(num_digits) 
                # Добавляем порядковый номер
            new_name += num
                
                # Добавляем расширение
            new_name += '.' + target_ext
                
                # Изменяем имя файла
            old_path = os.path.join(folder_path, file_name)
            new_path = os.path.join(folder_path, new_name)
            os.rename(old_path, new_path)


rename_files(desired_name="new_file_", num_digits=3, source_ext="txt", target_ext="doc")

# rename_files_2(desired_name="new_file_", num_digits=3, source_ext="txt", target_ext="doc")

folder_content = ""
files = os.listdir(folder_path)
separator = ", "
files_as_string = separator.join(files)
print(files_as_string)

# удаление папки
# shutil.rmtree(folder_path)