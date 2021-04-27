#coding:utf-8

#Урок-3 задание-3
'''
Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.
'''

def my_func(a, b, c):
    l = [a,b,c]
    m = sorted(l,reverse=True)
    m.pop()
    return sum(m)
print(my_func(17,9,13))