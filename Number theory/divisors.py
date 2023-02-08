from sortedcontainers import SortedSet
import math

n = 100
limit = int(math.sqrt(n)+1)
divisors = SortedSet()

for i in range(1, limit):
    if n%i == 0:
        divisors.add(i)
        divisors.add(n//i)
print(divisors)
