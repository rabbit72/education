a = int(input())
b = int(input())
c = int(input())
t = 0
if a - b == 0:
    t = t + 2
    if a - c == 0:
        t = t + 1
elif b - c == 0:
    t = t + 2
    if a - c == 0:
        t = t + 1
elif a - c == 0:
    t = t + 2
print(t)
