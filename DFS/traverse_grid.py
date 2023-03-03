image = [[1,1,1],[1,1,0],[1,0,1]]
sr, sc, color = 1, 1, 2
source = image[sr][sc]
rows, cols = len(image), len(image[0])

def track(i, j, grid):
    if i<0 or i>=rows or j<0 or j>=cols:
        return None
    if source!=grid[i][j] or grid[i][j]==color:
        return None
    grid[i][j] = color
    track(i-1, j, grid)
    track(i, j-1, grid)
    track(i+1, j, grid)
    track(i, j+1, grid)
track(sr, sc, image)
print(image)
