#coding:utf-8

#Урок-5 задание-4

my_dict = {'One': 'Один','Two': 'Два','Three': 'Три','Four': 'Четыре'}

with open("text_4.txt", "r", encoding = 'utf-8') as t:
    l = t.readlines()

with open("text_4_new.txt", "a", encoding = 'utf-8') as t_new:
    for line in l:
        s = line.split()
        s[0] = my_dict[s[0]]
        print(' '.join(s), file = t_new)