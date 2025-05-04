class Graph:
    def __init__(self, n):
        self.n = n
        self.adj = [[] for _ in range(n+1)]

    def add_edge(self, u, v):
        self.adj[u].append(v)
        self.adj[v].append(u)

    def remove_edge(self, u, v):
        self.adj[u].remove(v)
        self.adj[v].remove(u)

    def is_connected(self):
        visited = [False] * (self.n + 1)
        start = 1
        for i in range(1, self.n + 1):
            if self.adj[i]:
                start = i
                break
        if not self.adj[start]:
            return self.n == 1

        stack = [start]
        visited[start] = True
        count = 1
        while stack:
            u = stack.pop()
            for v in self.adj[u]:
                if not visited[v]:
                    visited[v] = True
                    stack.append(v)
                    count += 1
        return count == self.n


if __name__ == '__main__':
    f = open('input.txt', 'r')
    parts = f.readline().split()
    n = int(parts[0])
    m = int(parts[1])

    edges = [None]
    g = Graph(n)

    for i in range(m):
        a, b = map(int, f.readline().split())
        edges.append((a, b))
        g.add_edge(a, b)

    k = int(f.readline())
    for j in range(k):
        data = list(map(int, f.readline().split()))
        C = data[0]
        to_remove = data[1:]

        for eid in to_remove:
            u, v = edges[eid]
            g.remove_edge(u, v)

        if g.is_connected():
            print("Connected")
        else:
            print("Disconnected")

        for eid in to_remove:
            u, v = edges[eid]
            g.add_edge(u, v)

    f.close()