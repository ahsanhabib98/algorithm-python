import math

n = 50
digit = 0
for i in range(1, n+1):
    digit += math.log10(i)
print(int(digit)+1)
