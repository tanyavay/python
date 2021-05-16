#coding:utf-8

#Урок-6 задание-2

class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calc(self):
        return f'Масса равнв: {(self._length * self._width * 25 * 5) / 1000} т'

r = Road(5000, 20)
print(r.calc())
