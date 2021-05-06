#coding:utf-8

#Урок-4 задание-1

import sys
print(sys.argv)
path, hour, tarif, bonus = sys.argv
print(f'Ваша зарплата составила: {int(hour) * int(tarif) + int(bonus)}')