def dfs(u):
    visited[u] = 1
    for v in adj[u]:
        if visited[v] == 0:
            if dfs(v):
                return True
        elif visited[v] == 1:
            return True
    visited[u] = 2
    return False


if __name__ == "__main__":
    n = int(input())
    adj = [[] for i in range(n+1)]
    for i in range(1, n+1):
        row = list(map(int, input().split()))
        for j, v in enumerate(row, start=1):
            if v:
                adj[i].append(j)

    visited = [0] * (n+1)

    for u in range(1, n+1):
        if visited[u] == 0:
            if dfs(u):
                print(1)
                break
    else:
        print(0)
