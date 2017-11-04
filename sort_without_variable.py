a = int(input())
b = int(input())
c = int(input())
if a > c:
    a, c = c, a
    if b < a:
        a, b = b, a
        if b > c:
            b, c = c, b
            print(a, b, c)
        else:
            print(a, b, c)
    elif b > c:
        b, c = c, b
        print(a, b, c)
    else:
        print(a, b, c)
elif b < a:
    a, b = b, a
    if b > c:
        b, c = c, b
        print(a, b, c)
    else:
        print(a, b, c)
elif b > c:
    b, c = c, b
    print(a, b, c)
else:
        print(a, b, c)
