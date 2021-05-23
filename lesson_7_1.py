#coding:utf-8

#Урок-7 задание-1

a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
b = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

class Matrix:
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return '\n'.join('\t'.join([str(it) for it in line]) for line in self.data)

    def __add__(self, other):
        new = []
        for i in range(len(self.data)):
            new.append([])
            for j in range(len(self.data[0])):
                new[i].append(self.data[i][j] + other.data[i][j])
        return Matrix(new)

matr1 = Matrix(a)
matr2 = Matrix(b)
print(matr1)
print(matr1 + matr2)