s = "aab"
p = "a*b*c*"
cache = {}
def dfs(i, j):
    if (i, j) in cache:
        return cache[(i, j)]
    if i>=len(s) and j>=len(p):
        return True
    if j>=len(p):
        return False

    match = i<len(s) and (s[i]==p[j] or p[j]=='.')

    if j+1<len(p) and p[j+1]=='*':
        cache[(i, j)] = (dfs(i, j+2) or (match and dfs(i+1, j)))
        return cache[(i, j)]
    if match:
        return dfs(i+1, j+1)
    return False
print(dfs(0,0))
