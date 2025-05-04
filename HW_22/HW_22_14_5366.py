class Graph:
    def __init__(self, n):
        self.n = n
        self.adj = [[] for i in range(n+1)]

    def add_edge(self, u, v):
        self.adj[u].append(v)
        self.adj[v].append(u)

    def find_centroids(self):
        n = self.n
        parent = [0] * (n+1)
        subtree_size = [0] * (n+1)
        comp_max = [0] * (n+1)
        stack = [(1, 0, 0)]
        while stack:
            u, p, state = stack.pop()
            if state == 0:
                parent[u] = p
                stack.append((u, p, 1))
                for v in self.adj[u]:
                    if v != p:
                        stack.append((v, u, 0))
            else:
                subtree_size[u] = 1
                max_part = 0
                for v in self.adj[u]:
                    if v != parent[u]:
                        subtree_size[u] += subtree_size[v]
                        if subtree_size[v] > max_part:
                            max_part = subtree_size[v]
                rest = n - subtree_size[u]
                if rest > max_part:
                    max_part = rest
                comp_max[u] = max_part
        best = min(comp_max[1:])
        return [u for u in range(1, n+1) if comp_max[u] == best]

if __name__ == '__main__':
    tokens = list(map(int, input().split()))
    n = tokens[0]
    edge_tokens = tokens[1:]
    needed = 2*(n-1)
    while len(edge_tokens) < needed:
        edge_tokens.extend(map(int, input().split()))

    g = Graph(n)
    for i in range(n-1):
        u = edge_tokens[2*i]
        v = edge_tokens[2*i+1]
        g.add_edge(u, v)

    centroids = g.find_centroids()
    print(*centroids)
