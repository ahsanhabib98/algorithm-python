import math

def first_kind(n, k):
    if k == 1:
        return math.factorial(n-1)
    if n == k:
        return 1
    return first_kind(n-1, k-1) + (n-1)*first_kind(n-1, k)
print(first_kind(4, 2))
