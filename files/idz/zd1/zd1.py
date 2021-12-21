#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Написать программу, которая считывает текст из файла и определяет, сколько в нем слов,
состоящих из не менее чем семи букв.
'''

if __name__ == '__main__':
    with open('text.txt', 'r', encoding='utf-8') as file:
        content = file.readline().split()
        counter = 0
        for i in content:
            if len(i) >= 7:
                counter += 1
        if content == 0:
            print('В файле нет слов длиннее 7 символов')
        else:
            print(f'В файле {counter} слов длиннее 7-ми символов')
