class DSU:
    def __init__(self, n):
        self.parent = list(range(n+1))
    def find(self, x):
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x
    def union(self, x, y):
        x, y = self.find(x), self.find(y)
        if x == y: return False
        self.parent[y] = x
        return True

t = int(input())
for _ in range(t):
    n, m, p, q = map(int, input().split())
    edges = []
    pq_weight = None
    for _ in range(m):
        u, v, w = map(int, input().split())
        edges.append((w, u, v))
        if (u == p and v == q) or (u == q and v == p):
            pq_weight = w

    edges.sort()
    dsu = DSU(n)
    answer = "NO"

    for w, u, v in edges:
        if dsu.union(u, v):
            if (u == p and v == q) or (u == q and v == p):
                answer = "YES"
    print(answer)