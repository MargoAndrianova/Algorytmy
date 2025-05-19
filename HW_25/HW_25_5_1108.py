def has_negative_cycle(n, edges):
    INF = 10**18
    dist = [0] * n

    for i in range(n):
        changed = False
        for u, v, w in edges:
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                changed = True
                if i == n - 1:
                    return True
        if not changed:
            break
    return False

n, m = map(int, input().split())
edges = []
for _ in range(m):
    x, y, t = map(int, input().split())
    edges.append((x, y, t))

if has_negative_cycle(n, edges):
    print("possible")
else:
    print("not possible")
