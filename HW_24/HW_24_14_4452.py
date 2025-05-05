from collections import deque

n, m = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(n)]

start = (0, 0)

visited = [[False]*m for _ in range(n)]
q = deque()
q.append((start[0], start[1], 0))
visited[start[0]][start[1]] = True

dirs = [(1,0),(-1,0),(0,1),(0,-1)]

while q:
    r, c, d = q.popleft()
    for dr, dc in dirs:
        nr, nc = r, c
        while True:
            tr, tc = nr + dr, nc + dc
            if not (0 <= tr < n and 0 <= tc < m) or lab[tr][tc] == 1:
                break
            nr, nc = tr, tc
            if lab[nr][nc] == 2:
                print(d+1)
                exit()
        if not visited[nr][nc]:
            visited[nr][nc] = True
            q.append((nr, nc, d+1))

