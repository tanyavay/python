#coding:utf-8

#Урок-1 задание-5
rev = float(input('Введите выручку: '))
exp = float(input('Введите издержки: '))
profit = rev - exp
if rev - exp >= 0:
    r = profit / rev
    print('Рентабельность равна: {}'.format(r))
    staff = int(input('Введите численность сотрудников: '))
    rs = profit / staff
    print('Прибыль на сотрудника: {} руб./чел.'.format(rs))
else: print('Убыток равен: {}' .format (profit))