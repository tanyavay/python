#coding:utf-8

#Урок-4 задание-6

from itertools import count, cycle

n_1 = int(input("Введите первое число: "))
n_end = int(input("Введите последнее число: "))

for i in count(n_1):
    if i > n_end:
        break
    else:
        print(i)

l = input("Введите список через пробел: ").split()
iter = cycle(l)

print(next(iter))
print(next(iter))
print(next(iter))
print(next(iter))