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
prime_factors(660)
