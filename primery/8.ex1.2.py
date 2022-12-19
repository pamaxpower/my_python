from random import randint


class Matrix(list):
    def __init__(self, list_in):
        self.list_out = [line.copy() for line in list_in]

    def __str__(self):
        return '\n'.join(['\t'.join(map(str, line)) for line in self.list_out])

    def size(self):
        return len(self.list_out), len(self.list_out[0])

    def __add__(self, other):
        size_i, size_j = self.size()
        return Matrix([[self.list_out[i][j] + other.list_out[i][j] for j in range(size_j)] for i in range(size_i)])


size_i = 3
size_j = 5
lst1 = [[randint(0, 9) for _ in range(size_j)] for _ in range(size_i)]
lst2 = [[randint(0, 9) for _ in range(size_j)] for _ in range(size_i)]

m1 = Matrix(lst1)
print(m1, '\n')
m2 = Matrix(lst2)
print(m2, '\n')
print(m1 + m2)