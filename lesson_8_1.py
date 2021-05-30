#coding:utf-8

#Урок-8 задание-1

class Date:

    @classmethod
    def mydate(cls, obj):
        a = obj.split('-')
        my_date = [int(a[0]), int(a[1]), int(a[2])]
        return my_date

    @staticmethod
    def validate(obj):
        a = obj.split('-')
        if int(a[0]) <= 31 and int(a[0]) != 0 and int(a[1])<= 12 and int(a[1]) != 0 and int(a[2]) <= 2100:
            return f'Данные внесены верно'
        else:
            return f'Ошибка ввода данных'
d = '31-12-2021'
print(Date.mydate(d))
print(Date.validate(d))
