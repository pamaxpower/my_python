'''
Генерация случайных данных и нахождение корней квадратного уравнения


Создайте функцию generate_csv_file(file_name, rows), которая будет генерировать
по три случайны числа в каждой строке, от 100-1000 строк,
и записывать их в CSV-файл. Функция принимает два аргумента:

file_name (строка) - имя файла, в который будут записаны данные.
rows(целое число) - количество строк (записей) данных, которые нужно сгенерировать.


Создайте функцию find_roots(a, b, c), которая будет находить корни квадратного 
уравнения вида ax^2 + bx + c = 0. Функция принимает три аргумента:

a, b, c (целые числа) - коэффициенты квадратного уравнения.

Функция возвращает:
None, если уравнение не имеет корней (дискриминант отрицателен).
Одно число, если уравнение имеет один корень (дискриминант равен нулю).
Два числа (корни), если уравнение имеет два корня (дискриминант положителен).

Создайте декоратор save_to_json(func), который будет оборачивать функцию find_roots. 
Декоратор выполняет следующие действия:

Читает данные из CSV-файла, переданного в аргументе функции, исходя из аргумента args[0].

Для каждой строки данных вычисляет корни квадратного уравнения с помощью функции find_roots.

Сохраняет результаты в формате JSON в файл results.json. 
Каждая запись JSON содержит параметры a, b, c и результаты вычислений.

Таким образом, после выполнения функций generate_csv_file и find_roots в файле results.json будет сохранена 
информация о параметрах и результатах вычислений для каждой строки данных из CSV-файла.

Пример

generate_csv_file("input_data.csv", 101)
find_roots("input_data.csv")

with open("results.json", 'r') as f:
    data = json.load(f)

if 100<=len(data)<=1000:
    print(True)
else:
    print(f"Количество строк в файле не находится в диапазоне от 100 до 1000.")

print(len(data)==101)
'''


import csv
import json
from random import randint


def save_to_json(func):
    def wrapper(*args):
        res_list = []
        with open(args[0], 'r') as f_csv:
            file_read = csv.reader(f_csv)
            for row in file_read:
                a, b, c = map(int, row)
                result = func(a, b, c)
                dt = {'parameters': [a,b,c], 'result': result}
                res_list.append(dt)
        with open('result.json', 'w') as f_json:
            json.dump(res_list, f_json, indent=2, separators=(',', ' : '), ensure_ascii=False)
    return wrapper


@save_to_json
def find_roots(a, b, c):
    d = b ** 2 - 4 * a * c
    if d < 0:
        return None
    elif d == 0:
        x = -b / (2 * a)
        return x
    else:
        x1 = (-b + d ** 0.5) / (2 * a)
        x2 = (-b - d ** 0.5) / (2 * a)
        return x1, x2


def generate_csv_file(file_name, row):
    with open(file_name, 'w', newline='') as fn:
        csv_write = csv.writer(fn, dialect='excel')
        for i in range(row):
            ln = [randint(1, 1000) for _ in range(3)]
            csv_write.writerow(ln)


generate_csv_file("input_data.csv", 101)
find_roots("input_data.csv")

with open("result.json", 'r') as f:
    data = json.load(f)

if 100<=len(data)<=1000:
    print(True)
else:
    print(f"Количество строк в файле не находится в диапазоне от 100 до 1000.")

print(len(data)==101)
