#coding:utf-8

#Урок-3 задание-6
'''
не докрутила :(
'''
def int_func():
    l = input('Введите фразу на латинице строчными буквами: ')
    for i in l:
        i = ord(i)
        if i in range(ord('a'), ord('z')+1):
            return l.title()
        else: return print('Неверный ввод')
print(f'Получилось {int_func()}')
