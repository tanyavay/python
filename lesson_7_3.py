#coding:utf-8

#Урок-7 задание-3

class Cell:
    def __init__(self, num):
        self.num = num

    def __str__(self):
        return f'{self.num}'

    def __add__(self, other):
        return Cell(self.num + other.num)

    def __sub__(self, other):
        if self.num - other.num > 0:
            return Cell(self.num - other.num)
        else:
            print('Нельзя выполнить операцию вычитания')

    def __mul__(self, other):
        return Cell(self.num * other.num)

    def __truediv__(self, other):
        return Cell(self.num // other.num)

    def make_order(self, rows):
        return '\n'.join(['*' * rows for _ in range(self.num // rows)]) + '\n' + '*' * (self.num % rows)

cell1 = Cell(18)
cell2 = Cell(12)
print(cell1 + cell2)
print(cell1 * cell2)
print(cell1.make_order(5))