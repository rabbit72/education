a1 = int(input())
b1 = int(input())
c1 = int(input())
a2 = int(input())
b2 = int(input())
c2 = int(input())
v = [0, 1, 2, 3, 4, 5]
v[0] = (a1 // a2) * (b1 // b2) * (c1 // c2)
v[1] = (a1 // a2) * (b1 // c2) * (c1 // b2)
v[2] = (a1 // b2) * (b1 // a2) * (c1 // c2)
v[3] = (a1 // b2) * (b1 // c2) * (c1 // a2)
v[4] = (a1 // c2) * (b1 // a2) * (c1 // b2)
v[5] = (a1 // c2) * (b1 // b2) * (c1 // a2)
mx = v[0]
for i in range(6):
    if mx < v[i]:
        mx = v[i]
print(mx)
