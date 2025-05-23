import heapq

def solve():
    n, m, p = map(int, input().split())
    dangerous = set()
    if p > 0:
        dangerous = set(map(int, input().split()))
    edges = []
    if m > 0:
        for _ in range(m):
            u, v, w = map(int, input().split())
            edges.append((w, u, v))
    else:
        if n == 1:
            print(0)
        else:
            print("impossible")
        exit()

    if p == n:
        adj = [[] for _ in range(n + 1)]
        for w, u, v in edges:
            adj[u].append((w, v))
            adj[v].append((w, u))
        used = [False] * (n + 1)
        hq = [(0, 1)]
        total = 0
        cnt = 0
        while hq and cnt < n:
            w, u = heapq.heappop(hq)
            if used[u]:
                continue
            used[u] = True
            total += w
            cnt += 1
            for ww, v in adj[u]:
                if not used[v]:
                    heapq.heappush(hq, (ww, v))
        if cnt < n:
            print("impossible")
        else:
            print(total)
        return

    adj_safe = [[] for _ in range(n+1)]
    best_attach = [float('inf')] * (n+1)
    for w, u, v in edges:
        u_d = (u in dangerous)
        v_d = (v in dangerous)
        if not u_d and not v_d:
            adj_safe[u].append((w, v))
            adj_safe[v].append((w, u))
        elif u_d and not v_d:
            if w < best_attach[u]:
                best_attach[u] = w
        elif v_d and not u_d:
            if w < best_attach[v]:
                best_attach[v] = w

    safe_nodes = [u for u in range(1, n+1) if u not in dangerous]
    S = len(safe_nodes)

    if S == 0:
        print("impossible")
        return

    dist = [float('inf')] * (n+1)
    used = [False] * (n+1)
    start = safe_nodes[0]
    dist[start] = 0
    hq = [(0, start)]
    total_safe_cost = 0
    cnt_used = 0

    while hq and cnt_used < S:
        d, u = heapq.heappop(hq)
        if used[u]: continue
        used[u] = True
        total_safe_cost += d
        cnt_used += 1
        for w, v in adj_safe[u]:
            if not used[v] and w < dist[v]:
                dist[v] = w
                heapq.heappush(hq, (w, v))

    if cnt_used < S:
        print("impossible")
        return

    total_attach = 0
    for u in dangerous:
        w = best_attach[u]
        if w == float('inf'):
            print("impossible")
            return
        total_attach += w

    print(total_safe_cost + total_attach)

if __name__ == "__main__":
    solve()
