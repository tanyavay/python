#coding:utf-8

#Урок-5 задание-1

with open("text_1.txt", "w", encoding = 'utf-8') as t:
    while True:
        n = input("Введите слово: \n")
        if n == '':
            break
        t.write(n+ '\n')