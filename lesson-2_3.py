#coding:utf-8

#Урок-2 задание-3

d = dict(Зима=[12,1,2], Весна=[3,4,5], Лето=[6,7,8], Осень=[9,10,11])
month = int(input('Введите номер месяца: '))
if 1 <= month <= 12:
    for key, value in d.items():
        if month in value:
            print(f'Month name: {key}')
else: print('Месяца с таким номером не существует')
