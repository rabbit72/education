def sum_mark(list):  # функция суммы баллов
    return list[-1] + list[-2] + list[-3]


# ввод данных из файла
with open('input.txt', 'r', encoding='utf8') as f:
    n = int(f.readline())
    students = []
    for line in f:
        students.append(line.split())
# создание списка людей у кого нет <40 баллов
st_ok = []
for i in range(len(students)):
    flag = 0
    for j in range(-1, -4, -1):
        students[i][j] = int(students[i][j])
        if students[i][j] < 40:
            flag += 1
    if not flag:
        st_ok.append(students[i])
# сортировка по сумме баллов
st_ok.sort(key=sum_mark)
#  нахождение количества максимумов баллов
mx = sum_mark(st_ok[-1])
count = 0
st_sum = []
for i in range(len(st_ok)):
    st_sum.append(sum_mark(st_ok[i]))
    if st_sum[i] == mx:
        count += 1
# формируем результат
if n >= len(st_ok):
    result = 0
elif count > n:
    result = 1
else:
    while st_sum[-n] == st_sum[-(n + 1)]:
        n -= 1
    result = st_sum[-n]
# вывод результата в файл
with open('output.txt', 'w', encoding='utf8') as f:
    print(result, file=f)
