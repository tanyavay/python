#coding:utf-8

#Урок-8 задание-3

class Not_num(Exception):
    pass
my_list = []
while True:
    try:
        n = input('Введите число в список, для завершениея введите "*": ')
        if n == '*':
            break
        if not n.isdigit():
            raise Not_num(n)
        my_list.append(int(n))
    except Not_num as err:
        print('Не число!', err)
print(my_list)