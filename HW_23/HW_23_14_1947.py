class Graph:
    def __init__(self, n, directed=False):
        self.n = n
        self.directed = directed
        self.adj = [[] for _ in range(n+1)]
        self.indegree = [0] * (n+1)

    def add_edge(self, u, v):
        self.adj[u].append(v)
        if self.directed:
            self.indegree[v] += 1
        else:
            self.adj[v].append(u)

    def topological_sort(self):
        if not self.directed:
            raise ValueError
        from collections import deque
        q = deque()
        for u in range(1, self.n+1):
            if self.indegree[u] == 0:
                q.append(u)
        topo = []
        while q:
            u = q.popleft()
            topo.append(u)
            for v in self.adj[u]:
                self.indegree[v] -= 1
                if self.indegree[v] == 0:
                    q.append(v)
        return topo if len(topo) == self.n else None

    def is_connected(self):
        if self.directed:
            return False
        visited = [False] * (self.n+1)
        start = 1
        for i in range(1, self.n+1):
            if self.adj[i]:
                start = i
                break
        if not self.adj[start]:
            return self.n == 1
        stack = [start]
        visited[start] = True
        cnt = 1
        while stack:
            u = stack.pop()
            for w in self.adj[u]:
                if not visited[w]:
                    visited[w] = True
                    stack.append(w)
                    cnt += 1
        return cnt == self.n

def dfs1(u):
    visited[u] = True
    for v in g[u]:
        if not visited[v]:
            dfs1(v)
    order.append(u)

def dfs2(u):
    comp[u] = cid
    for v in gr[u]:
        if comp[v] == 0:
            dfs2(v)

if __name__ == '__main__':
    f = open('input.txt','r')
    n, m = map(int, f.readline().split())
    g = [[] for i in range(n+1)]
    gr = [[] for i in range(n+1)]
    edges = []

    for j in range(m):
        u, v = map(int, f.readline().split())
        g[u].append(v)
        gr[v].append(u)
        edges.append((u, v))

    visited = [False] * (n+1)
    order = []

    for u in range(1, n+1):
        if not visited[u]:
            dfs1(u)

    comp = [0] * (n+1)
    cid = 0

    for u in reversed(order):
        if comp[u] == 0:
            cid += 1
            dfs2(u)

    s = set()
    for u, v in edges:
        cu = comp[u]
        cv = comp[v]
        if cu != cv:
            s.add((cu, cv))

    cg = Graph(cid, directed=True)
    for cu, cv in s:
        cg.add_edge(cu, cv)

    cg.topological_sort()

    print(len(s))

    f.close()
