import math

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def union(self, x, y):
        x, y = self.find(x), self.find(y)
        if x != y:
            self.parent[y] = x
            return True
        return False

def solve_case(s, p, coords):
    edges = []
    for i in range(p):
        for j in range(i + 1, p):
            x1, y1 = coords[i]
            x2, y2 = coords[j]
            d = math.hypot(x1 - x2, y1 - y2)
            edges.append((d, i, j))
    edges.sort()
    dsu = DSU(p)
    mst_edges = []
    for dist, u, v in edges:
        if dsu.union(u, v):
            mst_edges.append(dist)
            if len(mst_edges) == p - 1:
                break
    mst_edges.sort(reverse=True)
    if len(mst_edges) < p - 1:
        return 0.0
    if s - 1 < len(mst_edges):
        answer = mst_edges[s - 1]
    else:
        answer = 0.0
    return answer

n = int(input())
for _ in range(n):
    s, p = map(int, input().split())
    coords = [tuple(map(int, input().split())) for _ in range(p)]
    result = solve_case(s, p, coords)
    print(f"{result:.2f}")
