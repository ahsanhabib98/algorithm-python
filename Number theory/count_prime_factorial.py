# Count prime number in factorial where prime number is 5

n = 100
ans = 0
p = 5
while p<=n:
    ans += n//p
    p *= p
print(ans)
