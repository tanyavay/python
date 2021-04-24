#coding:utf-8

#Урок-2 задание-2

l = input('Введите элементы списка через пробел: ').split()
i = 0
if len(l) % 2 == 0:
    while i < len(l):
        a = l[i]
        l[i] = l[i+1]
        l[i+1] = a
        i += 2
else:
    while i < len(l)-1:
        a = l[i]
        l[i] = l[i+1]
        l[i+1] = a
        i += 2
print(l)