#coding:utf-8

#Урок-8 задание-7

class ComplexNum:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return f'Сумма равна: {self.a + other.a} + {self.b + other.b} * i'

    def __mul__(self, other):
        return f'Произведение равно: {self.a * other.a - (self.b * other.b)} + {self.b * other.a} * i'


c_1 = ComplexNum(5, -10)
c_2 = ComplexNum(1, 3)
print(c_1 + c_2)
print(c_1 * c_2)