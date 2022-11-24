"""Напишите программу для проверки истинности утверждения
¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
"""
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z - закон Де Моргана
# ¬(X ⋁ Y ⋁ Z) по-другому чстается как not(X and Y and Z)
# ¬X ⋀ ¬Y ⋀ ¬Z читается как (not X) or (not Y) or (not Z)

predicate = [True, False]
for x in predicate:
    for y in predicate:
        for z in predicate:
            left = not (x and y and z)
            rigth = (not x) or (not y) or (not z)
            if left == rigth:
                print(f'Для {x,y,z} равенство верное')
            else:
                print(f'Для {x,y,z} равенство неверное')
