#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Разработайте программу, которая будет показывать слово
(или слова), чаще остальных встречающееся в текстовом файле.
Сначала пользователь должен ввести имя файла для обработки.
После этого вы должны открыть файл и проанализировать его построчно,
разделив при этом строки по словам и исключив из них пробелы и знаки препинания.
Также при подсчете частоты появления слов в файле вам стоит игнорировать регистры.
'''

import collections

if __name__ == '__main__':
    file_name = input('Введите имя файла с расширением: ')
    table = str.maketrans({',': None, '.': None, '!': None, '?': None})
    slova = collections.Counter()

    with open(file_name, 'r', encoding='utf-8') as file:
        for i in file:
            content = i.lower().translate(table).split()
            for path in content:
                slova[path] += 1

    print(
        slova.most_common(
            int(input("Сколько самых частых слов вы хотите увидеть? "))
        )
    )
