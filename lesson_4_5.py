#coding:utf-8

#Урок-4 задание-5

from functools import reduce
l = [i for i in range(100, 1001) if i % 2 == 0]
def my_func(prev_el, el):
    return prev_el * el

print(reduce(my_func, l))