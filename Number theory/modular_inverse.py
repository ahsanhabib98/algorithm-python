def bigmod(a, b, m):
    if b == 0: return 1 % m
    x = bigmod(a, b//2, m)
    x = (x*x) % m
    if b%2 == 1: x = (x*a) % m
    return x

# 8/2 = 4 mod 5
# as 2 and 5 coprime so 2^-1 = 2^(5-2) according to eular's theorem
ans = bigmod(2, 3, 5)*bigmod(2, 3, 5)%5
print(ans)
