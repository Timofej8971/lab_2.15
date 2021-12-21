#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys


if __name__ == '__main__':
    while True:
        command = input('Введите команду: ').lower()

        if command == 'exit':
            break

        elif command == 'check':
            file_path = input('Введите путь до проверяемого файла: ')
            f = os.access(file_path, os.F_OK)
            r = os.access(file_path, os.R_OK)
            w = os.access(file_path, os.W_OK)
            x = os.access(file_path, os.X_OK)
            print('Выбранный файл имеет следующие параметры доступа:  \n',
                  f, '\n', r, '\n', w, '\n', x, '\n'
                  )

        elif command == 'help':
            print('Cписок команд:\n'
                  'exit - выход из программы'
                  'check - проверка доступа'
                  'help - помощь'
                  )

        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)
