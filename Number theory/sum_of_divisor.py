n = 12
i = 2
p = []
while i * i <= n:
    if n % i:
        i += 1
    else:
        n //= i
        p.append(i)
if n > 1:
    p.append(n)

from collections import Counter
counts = dict(Counter(p))

sod = 1
for p, a in counts.items():
    sod *= ((p**(a+1))-1)/(p-1)
print(sod)
