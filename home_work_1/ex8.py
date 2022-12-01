"""Напишите программу для проверки истинности утверждения
¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
"""
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z - закон Де Моргана
# ¬(X ⋁ Y ⋁ Z) по-другому читается как not(X or Y or Z)
# ¬X ⋀ ¬Y ⋀ ¬Z читается как (not X) and (not Y) and (not Z)

predicate = [True, False]
for x in predicate:
    for y in predicate:
        for z in predicate:
            left = not (x or y or z)
            rigth = (not x) and (not y) and (not z)
            if left == rigth:
                print(f'Для {x,y,z} равенство верное')
            else:
                print(f'Для {x,y,z} равенство неверное')


# ⋁ - дизъюнкция (операция ИЛИ) = or
# ⋀ - конъюнкция (логическое И) = and