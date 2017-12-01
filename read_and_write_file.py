#  Блок чтения из файла с дальнейшем закрытием даже при ошибке
with open('input.txt', 'r', encoding='utf8') as f_input:
    n = int(f_input.readline())
    push_limit = list(map(int, f_input.readline().split()))
    k = int(f_input.readline())
    clicks = list(map(int, f_input.readline().split()))
for now in clicks:
    push_limit[now - 1] -= 1
#  Блок записи в файл с дальнейшем закрытием даже при ошибке
with open('output.txt', 'w', encoding='utf8') as f_output:
    for now in push_limit:
        if now >= 0:
            print('NO', file=f_output)
        else:
            print('YES', file=f_output)

'''f_input = open('input.txt', 'r', encoding='utf8')
members = []
for temp_man in f_input:
    members.append(list(temp_man.split()))
f_input.close()
f_output = open('output.txt', 'w', encoding='utf8')
for line in members:
    f_output.write((' '.join(map(str, line))) + '\n')
f_output.close()'''
