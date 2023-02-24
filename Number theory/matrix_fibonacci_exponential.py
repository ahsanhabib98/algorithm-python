def matrix_multiply(a, b):
    n = 2
    c = [[0 for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                c[i][j] += a[i][k] * b[k][j]
    return c
    

result = [[1, 0], [0, 1]]
base = [[1, 1], [1, 0]]
v = [[1], [0]]
power = 19
while power>0:
    if power&1:
        result = matrix_multiply(result, base)
        power -= 1
    else:
        base = matrix_multiply(base, base)
        power //= 2
print(result[0][0] * v[0][0] + result[0][1] * v[1][0])
