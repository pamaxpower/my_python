"""
Как ходит шахматная фигура 'Ладья'
"""

x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())  # вводим координаты точек. x1 - начальная, x2 - конечная

# Ладья ходит на любое количество клеток по одной линии: т.е. X = const или Y = const

if x1 == x2 or y1 == y2:      # Так ходит ладья
    print('YES')
else:
    print('NO')

# if (x1==x2 and y1!=y2) or (y1==y2 and x1!=x2):
