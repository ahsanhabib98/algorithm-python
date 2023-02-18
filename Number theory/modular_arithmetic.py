# 1 + a + a^2 + .... + a^n mod 17

def bigmod(a, b, m):
    if b == 0: return 1 % m
    x = bigmod(a, b//2, m)
    x = (x*x) % m
    if b%2 == 1: x = (x*a) % m
    return x

ans = 0
for i in range(99):
    ans += bigmod(2, i, 17)
print(ans%17)
