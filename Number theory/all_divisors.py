n = 10+1
all_divisors = {}

for i in range(1, n):
    all_divisors[i] = []
    for j in range(i, n, i):
        all_divisors[i].append(j)
        
print(all_divisors)
