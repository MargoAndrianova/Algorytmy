from collections import deque

class Graph:
    def __init__(self, n):
        self.n = n
        self.adj = [[] for i in range(n+1)]

    def add_edge(self, u, v):
        self.adj[u].append(v)
        self.adj[v].append(u)

    def fire_spread(self, starts):

        dist = [-1] * (self.n + 1)
        q = deque()
        for s in starts:
            dist[s] = 0
            q.append(s)
        while q:
            u = q.popleft()
            for v in self.adj[u]:
                if dist[v] == -1:
                    dist[v] = dist[u] + 1
                    q.append(v)
        return dist


if __name__ == '__main__':
    n, m = map(int, input().split())
    g = Graph(n)

    for i in range(m):
        u, v = map(int, input().split())
        g.add_edge(u, v)

    k = int(input())
    starts = list(map(int, input().split()))
    dist = g.fire_spread(starts)

    max_time = max(dist[1:])
    last_vert = min(i for i in range(1, n+1) if dist[i] == max_time)
    print(max_time)
    print(last_vert)
