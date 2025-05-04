from collections import deque

class Graph:
    def __init__(self, matrix):
        self.matrix = matrix
        self.n = len(matrix)

    def bfs_distances(self, start):
        dist = [-1] * self.n
        dist[start] = 0
        q = deque([start])
        while q:
            u = q.popleft()
            for v in range(self.n):
                if self.matrix[u][v] == 1 and dist[v] == -1:
                    dist[v] = dist[u] + 1
                    q.append(v)
        return dist

if __name__ == '__main__':
    n, x = map(int, input().split())
    x -= 1

    matrix = [list(map(int, input().split())) for _ in range(n)]

    g = Graph(matrix)
    distances = g.bfs_distances(x)
    print(' '.join(map(str, distances)))
