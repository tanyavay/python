#coding:utf-8

#Урок-2 задание-5

n = int(input('натуральное число: '))
l = [7, 5, 3, 3, 2]
c = l.count(n)
for el in l:
    if c > 0:
        i = l.index(n)
        l.insert(i+c, n)
        break
    else:
        if n > el:
            j = l.index(el)
            l.insert(j, n)
            break
        elif n < l[len(l) - 1]:
            l.append(n)
print(l)