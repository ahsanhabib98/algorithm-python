w = 50
arr = [(20, 100), (10, 60), (30, 120)]
arr.sort(key = lambda x:x[1]/x[0], reverse=True)

ans = 0
for weight, price in arr:
    if weight<w:
        w -= weight
        ans += price
    else:
        ans += (price/weight)*w
print(ans)
