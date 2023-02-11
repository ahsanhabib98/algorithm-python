def egcd(a, b):
    if a == 0:
        return 0, 1
    x1, y1 = egcd(b%a, a)
    y = x1
    x = y1-((b//a)*x1)
    return x, y
x, y = egcd(10, 6)
print(x, y)
