n = 11
i = 2
ret = n
while i * i <= n:
    if n % i:
        i += 1
    else:
        while n%i==0:
            n //= i
        ret -= ret//i
if n > 1:
    ret -= ret//n
print(ret)
