from queue import Queue

adj_list = {
    "A": ["B", "D"],
    "B": ["A", "C"],
    "C": ["B"],
    "D": ["A", "E", "F"],
    "E": ["D", "F", "G"],
    "F": ["D", "E", "H"],
    "G": ["E", "H"],
    "H": ["G", "F"]
}

visited = {}
level = {}
parent = {}
traverse = []
queue = Queue()

for node in adj_list.keys():
    visited[node] = False
    parent[node] = None
    level[node] = -1

ch = "A"
visited[ch] = True
level[ch] = 0
queue.put(ch)

while not queue.empty():
    u = queue.get()
    traverse.append(u)
    for v in adj_list[u]:
        if not visited[v]:
            visited[v] = True
            parent[v] = u
            level[v] = level[u]+1
            queue.put(v)

# Traverse path
print("Traverse ",traverse)

# Shortest distance of all nodes from source node
# Level
print("Shortest distance from source node ",level["H"])

# Shortest path of any node from source node
v = "H"
path = []
while v is not None:
    path.append(v)
    v = parent[v]
print("Shortest path from source node ",path)
