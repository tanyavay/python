#coding:utf-8

#Урок-3 задание-5

def my_func():
    a = 0
    while True:
        l = input('Введите элементы списка через пробел, для завершения введите *: ').split()
        for i in l:
            try:
                if i == '*':
                    print(f'Итоговая сумма равна {a}')
                    return
                else:
                    a += int(i)
            except ValueError:
                print('Введите число или *')
        print(f'Сумма равна {a}')
print(my_func())