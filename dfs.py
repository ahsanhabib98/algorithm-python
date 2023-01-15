adj_list = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["B", "F"],
    "D": [],
    "E": ["F"],
    "F": []
}
    
color = {}    # W, G, B
parent = {}
traverse_time = {}    # [start, end]
traverse = []

for node in adj_list.keys():
    color[node] = "W"
    parent[node] = None
    traverse_time[node] = [-1, -1]
    
time = 0
def dfs(u):
    global time
    color[u] = "G"
    traverse_time[u][0] = time
    traverse.append(u)
    time += 1
    for v in adj_list[u]:
        if color[v] == 'W':
            parent[v] = u
            dfs(v)
    color[u] = "B"
    traverse_time[u][1] = time
    time += 1
    
dfs("A")
print(traverse)
print(parent)
print(traverse_time)

for node in adj_list.keys():
    print(node, " -> ", traverse_time[node])
