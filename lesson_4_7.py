#coding:utf-8

#Урок-4 задание-7

def fact(n):
    num = 1
    for i in range(1, n + 1):
        num *= i
        yield num

n = int(input("Введите число для расчета факториала: "))
for el in fact(n):
    print(el)