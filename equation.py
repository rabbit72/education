a = int(input())
b = int(input())
c = int(input())
d = int(input())
if a == 0 and b == 0:
    print('INF')
elif (a == c and b == d) or (a == 0 and b != 0):
    print('NO')
elif b % a == 0:
    x = int(-b / a)
    if c * x + d == 0:
        print('NO')
    else:
        print(x)
else:
    print('NO')
