k = int(input())
m = int(input())
n = int(input())
if n <= k:
    print(2 * m)
elif (2 * n) % k == 0:
    print(((n * 2) // k) * m)
else:
    print(((n * 2) // k) * m + m)
