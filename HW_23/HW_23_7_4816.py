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
        if len(topo) == self.n:
            return topo
        return None


if __name__ == '__main__':
    f = open('input.txt', 'r')
    parts = f.readline().split()
    n = int(parts[0])
    M = int(parts[1])
    g = Graph(n, directed=False)
    edges = []

    for j in range(M):
        u, v = map(int, f.readline().split())
        g.add_edge(u, v)
        edges.append((u, v))

    visited = [False] * (n+1)
    components = []

    for i in range(1, n+1):
        if not visited[i]:
            stack = [i]
            visited[i] = True
            comp = []
            while stack:
                u = stack.pop()
                comp.append(u)
                for w in g.adj[u]:
                    if not visited[w]:
                        visited[w] = True
                        stack.append(w)
            components.append(comp)

    print(len(components))
    for comp in components:
        print(len(comp))
        print(*comp)

    f.close()
