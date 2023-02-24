result = 1
base = 2
power = 1000000000000000000000000000000000000000000000000000000000000000000000009
mod = 10**9+7
while power>0:
    if power&1:
        result = (result*base)%mod
        power -= 1
    else:
        base = (base*base)%mod
        power //= 2
print(result)
