#coding:utf-8

#Урок-3 задание-1

a = float(input('Введите знаменатель '))
b = float(input('Введите числитель '))
if b == 0:
    print("Деление на ноль невозвможно")
else:
    def f_1(a, b):
        return a/b
    print(f'Результат деления равен {f_1(a, b)}')
