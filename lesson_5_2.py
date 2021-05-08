#coding:utf-8

#Урок-5 задание-2

with open("text_2.txt", "r", encoding = 'utf-8') as t:
    num_lines = 0
    num_words = 0
    for line in t:
        num_lines += 1
        num_words += len(line.split())
    print(f'Всего строк в файле: {num_lines}\nВсего слов в файле: {num_words}\n')

with open("text_2.txt", "r", encoding = 'utf-8') as t:
    i_line = 0
    for line in t:
        i_line += 1
        print(f'Количество слов в строке {i_line}: {len(line.split())}')