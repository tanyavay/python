#coding:utf-8

#Урок-4 задание-2

l = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_l = [j for i, j in zip(l, l[1:]) if j > i]
print(new_l)