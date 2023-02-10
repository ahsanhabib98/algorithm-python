def bigmod(a, b, m):
    if b == 0: return 1 % m
    x = bigmod(a, b//2, m)
    x = (x*x) % m
    if b%2 == 1: x = (x*a) % m
    return x

ans = bigmod(2, 100000000000000000000000000000000, 9)
print(ans)
