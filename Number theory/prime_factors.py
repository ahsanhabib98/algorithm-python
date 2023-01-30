n = 864
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
print(p)
