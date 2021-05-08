#coding:utf-8

#Урок-5 задание-6

my_dict = {}
with open("text_6.txt", "r", encoding = 'utf-8') as t:
    for line in t:
        s = line.split()
        num = "".join(el if el.isdigit() else " " for el in line).split()
        n = [int(item) for item in num]
        summ = sum(n)
        my_dict[s[0]] = summ
    print(my_dict)