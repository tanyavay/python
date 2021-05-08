#coding:utf-8

#Урок-5 задание-3

with open("text_3.txt", "r", encoding = 'utf-8') as t:
    salary = []
    list = []
    for line in t:
        s = line.split()
        if int(s[-1]) < 20000:
            list.append(s[0])
        salary.append(s[-1])
    n_list = ', '.join(list)
print(f'Сотрудники с окладом менее 20 000 руб.: {n_list}\nCредняя величина дохода сотрудников: {sum(map(int, salary)) / len(salary)}')