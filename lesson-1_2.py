#coding:utf-8

#Урок-1 задание-2

answ = int(input('Введите время в секундах:'))
hours = answ // 3600
minutes = answ // 60 % 60
seconds = answ % 60
print('Время в формате "чч:мм:сс" составит: %02d:%02d:%02d' % (hours, minutes, seconds))