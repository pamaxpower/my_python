'''
Напишите функцию для транспонирования матрицы 
transposed_matrix, 
принимает в аргументы matrix, 
и возвращает транспонированную матрицу.
'''

def transpose(matr):
    ""
    rows = len(matr)
    cols = len(matr[0])

    transposed = [[0 for _ in range(rows)] for _ in range(cols)]

    for i in range(rows):
        for j in range(cols):
            transposed[j][i] = matr[i][j]
    return transposed


matrix = [[1, 2, 3],
         [4, 5, 6], 
         [7, 8, 9]]

print(transpose(matrix))
