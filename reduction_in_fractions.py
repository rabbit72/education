def greatest_common_divisor(p, q):
    if p == q:
        return p
    elif p != 0 and q != 0:
        if p > q:
            return greatest_common_divisor(p % q, q)
        else:
            return greatest_common_divisor(p, q % p)
    else:
        return p + q


def reduce_fraction(p, q):
    d = greatest_common_divisor(n, m)
    p, q = p // d, q // d
    return print(p, q)


n = int(input())
m = int(input())
reduce_fraction(n, m)
