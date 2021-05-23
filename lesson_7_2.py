#coding:utf-8

#Урок-7 задание-2

from abc import ABC, abstractmethod

class Clothes(ABC):

    def __init__(self):
        pass

    @property
    @abstractmethod
    def consumption(self):
        pass

    def __add__(self, other):
        return self.consumption + other.consumption

class Coat(Clothes):
    def __init__(self, size):
        super().__init__()
        self.size = size

    @property
    def size(self, size):
        return self.__size

    @size.setter
    def size(self, size):
        if size < 40:
            print('Минимальный размер 40')
            self.__size = 40
        elif size > 56:
            print('Максимальный размер 56')
            self.__size = 56
        else:
            self.__size = size

    @property
    def consumption(self):
        return self.__size / 6.5 + 0.5


class Costume(Clothes):
    def __init__(self, height):
        super().__init__()
        self.height = height

    @property
    def height(self, height):
        return self.__height

    @height.setter
    def height(self, height):
        if height < 150:
            print('Минимальный рост 150')
            self.__height = 150
        elif height > 220:
            print('Максимальный рост 220')
            self.__height = 220
        else:
            self.__height = height

    @property
    def consumption(self):
        return self.__height / 100 * 2 + 0.3

coat1 = Coat(int(input('Размер пальто: ')))
print(f'Вам нужно {coat1.consumption:.2f} метров ткани для пальто')
cost1 = Costume(int(input('Рост для костюма (см): ')))
print(f'Вам нужно {cost1.consumption:.2f} метров ткани для костюма')
print(f'Всего нужно {coat1 + cost1:.2f} метров ткани на пальто и костюм')