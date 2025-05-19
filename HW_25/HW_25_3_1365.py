import heapq

n, s, f = map(int, input().split())
s -= 1
f -= 1

adj_matrix = [list(map(int, input().split())) for _ in range(n)]

INF = 10**18
dist = [INF] * n
dist[s] = 0

heap = [(0, s)]

while heap:
    d_u, u = heapq.heappop(heap)
    if d_u > dist[u]:
        continue
    if u == f:
        break
    for v in range(n):
        w = adj_matrix[u][v]
        if w >= 0:
            nd = d_u + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(heap, (nd, v))

print(dist[f] if dist[f] != INF else -1)