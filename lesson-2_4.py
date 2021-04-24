#coding:utf-8

#Урок-2 задание-4

l = input('Введите строку из нескольких слов: ').split()
for i, j in enumerate(l, 1):
        print(i, j[0:10])