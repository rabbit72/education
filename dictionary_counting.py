f = open('input.txt', 'r', encoding='utf8')
count = {}
for line in f:
    words = line.split()
    for n in words:
        count[n] = count.get(n, 0) + 1
f.close()
