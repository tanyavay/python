#coding:utf-8

#Урок-5 задание-5

with open("text_5.txt", "w", encoding='utf-8') as t:
    a = 0
    l = input('Введите числа через пробел: ').split()
    for i in l:
        a += int(i)
    a = str(a)
    t.write(a)