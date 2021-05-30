#coding:utf-8

#Урок-8 задание-2

class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt

a = input("Введите числитель: ")
b = input("Введите знаменатель: ")

try:
    a = int(a)
    b = int(b)
    if b == 0:
        raise OwnError("Деление на ноль невозможно")
except ValueError:
    print("Вы ввели не число")
except OwnError as err:
    print(err)
else:
    print(f"Все хорошо. Ваше число: {a/b}")
