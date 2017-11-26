def merge(a, b):
    c = []
    ia, ib = 0, 0
    while True:
        if ia < len(a) and ib < len(b):
            if a[ia] > b[ib]:
                c.append(b[ib])
                ib += 1
            else:
                c.append(a[ia])
                ia += 1
        elif ia < len(a) and ib == len(b):
            c.append(a[ia])
            ia += 1
        elif ib < len(b) and ia == len(a):
            c.append(b[ib])
            ib += 1
        else:
            break
    return c


l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))
print(*merge(l1, l2))
