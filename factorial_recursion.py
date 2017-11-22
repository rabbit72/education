def fact(a):
    if a < 2:
        return 1
    a *= fact(a - 1)
    return a