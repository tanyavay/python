#coding:utf-8

#Урок-1 задание-5
a = float(input('Введите результат 1-го дня: '))
b = float(input('Введите минимальную цель: '))
i = 0.1
day = 1
while a < b:
    a = a * (1 + i)
    day += 1
    print(day)