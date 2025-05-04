from collections import deque

class Graph:
    def __init__(self, n, directed=False):
        self.n = n
        self.directed = directed
        self.adj = [[] for i in range(n+1)]
        self.indegree = [0] * (n+1)

    def add_edge(self, u, v):
        self.adj[u].append(v)
        if self.directed:
            self.indegree[v] += 1
        else:
            self.adj[v].append(u)

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

    def topological_sort(self):
        if not self.directed:
            raise ValueError
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
        if len(topo) == self.n:
            return topo
        else:
            return None


if __name__ == '__main__':
    n, m = map(int, input().split())
    g = Graph(n, directed=True)
    for _ in range(m):
        u, v = map(int, input().split())
        g.add_edge(u, v)

    order = g.topological_sort()
    if order is None:
        print(-1)
    else:
        print(*order)
