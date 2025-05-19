def hamming(s, t):
    """Повертає кількість відмінних позицій рядків s і t однакової довжини."""
    cnt = 0
    for a, b in zip(s, t):
        if a != b:
            cnt += 1
    return cnt

n, k = map(int, input().split())
dna = [input().strip() for _ in range(n)]

INF = 1 << 31
in_mst = [False]*n
key = [INF]*n
parent = [-1]*n

key[0] = 0

total_cost = 0
edges = []

for _ in range(n):
    u = -1
    best = INF
    for i in range(n):
        if not in_mst[i] and key[i] < best:
            best = key[i]
            u = i
    in_mst[u] = True
    total_cost += key[u]
    if parent[u] != -1:
        edges.append((parent[u], u))
    for v in range(n):
        if not in_mst[v]:
            w = hamming(dna[u], dna[v])
            if w < key[v]:
                key[v] = w
                parent[v] = u

print(total_cost)
for u, v in edges:
    print(u, v)
