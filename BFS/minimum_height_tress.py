class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 0:
            return []
        if n == 1:
            return [0]
        if n == 2:
            return [0, 1]
        adj = defaultdict(list)
        degree = [0]*n
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
            degree[a] += 1
            degree[b] += 1

        leaves = deque([i for i in range(n) if degree[i] == 1])
        rem = n
        while rem > 2:
            rem -= len(leaves)
            for _ in range(len(leaves)):
                leaf = leaves.popleft()
                for nei in adj[leaf]:
                    degree[nei] -= 1
                    if degree[nei] == 1:
                        leaves.append(nei)
        return list(leaves)