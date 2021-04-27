#coding:utf-8

#Урок-3 задание-4

# функции отрабатывают, но не понимаю как убрать "None" в результате

def my_func(x,y):
    if x != float(abs(x)) or y != int(y):
        print ('Введены неверные значения x и y')
    else:
        y = -abs(y)
        return x**y
print(my_func(2,2.5))

def my_func_2(x,y):
    if x != float(abs(x)) or y != int(y):
        print ('Введены неверные значения x и y')
    else:
        y = abs(y)
        z = 1
        a = 1
        while z < y:
            z += 1
            a /= x
        return print(a)
print(my_func_2(2,-2))
