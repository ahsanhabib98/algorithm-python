import math

n = 100

prime = []
mark = [0]*(n+1)
limit = math.sqrt(n)+1

mark[1] = 1
for i in range(4, n+1, 2):
    mark[i] = 1

prime.append(2)
for i in range(3, n+1, 2):
    if not mark[i]:
        prime.append(i)
        if i<=limit:
            j = i*i
            while j<=n:
                mark[j] = 1
                j += i*2
print(prime)
