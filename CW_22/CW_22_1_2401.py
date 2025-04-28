class Graph:
    def __init__(self, matrix):
        self.matrix = matrix
        self.n = len(matrix)

    def neighbors(self, u):
        return [v for v, has_edge in enumerate(self.matrix[u]) if has_edge == 1]

    def bfs(self, start, end):
        dist = [-1] * self.n
        dist[start] = 0
        q = deque([start])
        while q:
            u = q.popleft()
            if u == end:
                return dist[u]
            for v in self.neighbors(u):
                if dist[v] == -1:
                    dist[v] = dist[u] + 1
                    q.append(v)
        return -1


from collections import deque


if __name__ == '__main__':
    n, s, f = map(int, input().split())
    s -= 1
    f -= 1
    matrix = [list(map(int, input().split())) for i in range(n)]
    g = Graph(matrix)
    distance = g.bfs(s, f)
    print(distance if distance != -1 else 0)
