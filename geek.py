import os
import psutil
print('Я умею:')
print(' [1] - я выведу список файлов')
print(' [2] - выведу информацию о системе')
print(' [3] - выведу список процессов')
do = int(input('Выберите действие: '))
if do == 1:
    print(os.listdir())
elif do == 2:
    print(os.name)
elif do == 3:
    print(psutil.pids())
else:
    pass
