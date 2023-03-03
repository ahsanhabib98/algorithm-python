grid = [[1,1,1,0,0], [1,1,0,0,0], [1,1,0,0,0], [0,0,0,1,1]]

rows, cols = len(grid), len(grid[0])
visited = set()
island = 0

def bfs(row, col):
    import collections
    queue = collections.deque()
    visited.add((row, col))
    queue.append((row, col))
    while queue:
        r, c = queue.popleft()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        for rd, cd in directions:
            row, col = r+rd, c+cd
            if row in range(rows) and col in range(cols) and grid[row][col]==1 and (row, col) not in visited:
                visited.add((row, col))
                queue.append((row, col))

for i in range(rows):
    for j in range(cols):
        if grid[i][j]==1 and (i, j) not in visited:
            bfs(i, j)
            island += 1
print(island)
