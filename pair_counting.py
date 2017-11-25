def fact(a):
    if a < 2:
        return 1
    a *= fact(a - 1)
    return a


def combination(a):
    result = fact(a) / (2 * fact(a - 2))
    return int(result)


result = 0
a = list(map(int, input().split()))
b = []
for n in a:
    if n not in b:
        b.append(n)
for n in b:
    result += combination(a.count(n))
print(result)
