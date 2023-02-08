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

nod = 1
for p, a in counts.items():
    nod *= a+1
print(nod)
