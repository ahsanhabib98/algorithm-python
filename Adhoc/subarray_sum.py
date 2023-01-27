nus = [1, -1, 0]
k = 0
add = 0
ans = 0
track = {}
for num in nums:
    add += num
    if add == k:
        ans += 1
    if add-k in track:
        ans += track[add-k]
    if add in track:
        track[add] += 1
    else:
        track[add] = 1
print(ans)
