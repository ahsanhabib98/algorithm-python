adj_list = {
    "A": ["C", "B"],
    "B": ["D"],
    "C": [],
    "D": ["A", "E"],
    "E": []
}
    
color = {}    # W, G, B
parent = {}

for node in adj_list.keys():
    color[node] = "W"
    parent[node] = None
    
def dfs(u, color, parent):
    color[u] = "G"
    
    for v in adj_list[u]:
        if color[v] == 'W':
            cycle = dfs(v, color, parent)
            if cycle == True:
                return True
        elif color[v] =='G':
            return True
    color[u] = "B"
    return False

is_cycle = False
for u in adj_list.keys():
    if color[u] == "W":
        is_cycle = dfs(u, color, parent)
        if is_cycle == True:
            break
print("Is cycle ", is_cycle)
