def second_kind(n, k):
    if k == 1 or n == k:
        return 1
    return second_kind(n-1, k-1) + k*second_kind(n-1, k)
print(second_kind(5, 3))
