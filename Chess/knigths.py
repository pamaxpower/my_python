"""
Как ходит шахматная фигура 'Конь'
"""

x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())  # вводим координаты точек. x1 - начальная, x2 - конечная

# Конь ходит буквой "Г": 2 шага по X и 1 по Y, или наоборот

step_x = x2 - x1                # считаем на сколько клеток он пошел по оси X
if step_x > 0:                  # проверка на модуль
    step_x = step_x
else:
    step_x = -step_x
# step_x = abs(x2-x1)
    
step_y = y2 - y1                # считаем на сколько клеток он пошел по оси Y
if step_y > 0:
    step_y = step_y
else:
    step_y = -step_y

if step_x == 2 and step_y == 1:            # Проверка на одинаковый шаг
    print('YES')
elif step_x == 1 and step_y == 2:
    print('YES')
else:
    print('NO')