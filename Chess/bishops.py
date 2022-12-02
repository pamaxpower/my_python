"""
Как ходит шахматная фигура 'Слон'
"""

x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())  # вводим координаты точек. x1 - начальная, x2 - конечная

# Слон ходит по диагонали на любое количество клеток: x и y меняются одинаково

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

if step_x == step_y:            # Проверка на одинаковый шаг. Если true - то так можно ходить
    print('YES')
else:
    print('NO')