#coding:utf-8

#Урок-6 задание-1

from time import sleep

class Traficlight:
    __color = ['красный','желтый','зеленый']

    def running(self):
        print('Горит', self.__color[0], 'свет')
        sleep(7)
        print('Горит', self.__color[1], 'свет')
        sleep(2)
        print('Горит', self.__color[2], 'свет')
        sleep(4)

tl = Traficlight()
tl.running()