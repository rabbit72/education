import os
import sys
import psutil
import shutil

answer = ''
while answer != 'q':
    answer = input('Хочешь поработать? y/n/q')
    if answer == 'y':
        print('Я умею:')
        print(' [1] - я выведу список файлов')
        print(' [2] - выведу информацию о системе')
        print(' [3] - выведу список процессов')
        print(' [4] - продублирую файлы в директории')
        do = int(input('Выберите действие: '))
        if do == 1:
            print(os.listdir())
        elif do == 2:
            print('Текущая директория', os.getcwd())
            print('Версию платформы', sys.platform)
            print('Кодировка файловой сисиетмы', sys.getfilesystemencoding())
            print('Логин текущего пользователя', os.getlogin())
            print('Количество CPU', psutil.cpu_count())
        elif do == 3:
            print(psutil.pids())
        elif do == 4:
            print('Дублирование файлов в директории = ')
            fileName = os.listdir()
            for f in fileName:
                newFileName = f + '.test'
                shutil.copy(f, newFileName)

        else:
            pass
