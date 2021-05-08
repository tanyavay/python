#coding:utf-8

#Урок-5 задание-7

import json

with open("text_7.txt", "r", encoding = 'utf-8') as t:
    #print(t.read())
    prof = []
    my_dict = {}
    av_prof_dict = {}
    a = []
    for line in t:
        name, form, revenue, expense = line.split()
        profit = int(revenue) - int(expense)
        #print(profit)
        if profit >= 0:
            prof.append(profit)
        my_dict[name] = profit
        av_prof = round(sum(map(int, prof))/len(prof),2)
        av_prof_dict['average_profit'] = av_prof
    a.append(my_dict)
    a.append(av_prof_dict)
    print(a)

with open('text_7.json', 'w') as js:
    json.dump(a, js)