from collections import Counter
n = int(input())
a = list(map(int,input().split()))
a.sort()
counts = dict(Counter(a))
for i in a:
    if i-1 in counts:
        counts[i-1] -= 1
        if counts[i-1]<0:
            counts[i-1] = 0
print(sum(counts.values()))
