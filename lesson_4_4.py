#coding:utf-8

#Урок-4 задание-4

l =  [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
new_l = [i for i in l if l.count(i) < 2]
print(new_l)