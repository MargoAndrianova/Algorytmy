class Graph:
    def __init__(self, adj_list):
        self.adj = adj_list
        self.n = len(adj_list)

    def neighbors(self, u):
        return self.adj[u]

    def bfs(self, start, end):
        dist = [-1] * self.n
        parent = [None] * self.n
        q = deque([start])
        dist[start] = 0
        while q:
            u = q.popleft()
            if u == end:
                break
            for v in self.neighbors(u):
                if dist[v] == -1:
                    dist[v] = dist[u] + 1
                    parent[v] = u
                    q.append(v)
        return dist, parent


from collections import deque


if __name__ == '__main__':
    n, m = map(int, input().split())
    a, b = map(int, input().split())
    a -= 1
    b -= 1

    adj = [[] for i in range(n)]
    for i in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        adj[u].append(v)
        adj[v].append(u)

    g = Graph(adj)
    dist, parent = g.bfs(a, b)

    if dist[b] == -1:
        print(-1)
    else:
        path = []
        cur = b
        while cur is not None:
            path.append(cur + 1)
            cur = parent[cur]
        path.reverse()
        print(len(path) - 1)
        print(*path)