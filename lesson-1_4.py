#coding:utf-8

#Урок-1 задание-4
n = int(input('Введите целое положительное число n: '))
while n > 0:
    a = n % 10
    n = n // 10
    if n % 10 > a:
        a = n % 10
    n = n // 10
print(a)

