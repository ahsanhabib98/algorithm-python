import math
queries = [[2,6],[5,1],[73,660],[1,1],[2,2],[3,3],[4,4],[5,5]]
def prime_factors(n):
    i = 2
    pc = []
    while i * i <= n:
        cnt = 0
        while n%i == 0:
            cnt += 1
            n //= i
        if cnt>0:
            pc.append(cnt)
        i += 1
    if n > 1:
        pc.append(1)
    return pc
result = []
mod = 10**9+7
for n, k in queries:
    ans = 1
    for cnt in prime_factors(k):
        ans *= math.comb(cnt+n-1,n-1)
        ans %= mod
    result.append(ans)
print(result)
