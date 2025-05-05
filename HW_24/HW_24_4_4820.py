from collections import deque

N, M = map(int, input().split())
grid = [input().split() for _ in range(N)]
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())

sr, sc = y1-1, x1-1
tr, tc = y2-1, x2-1

if grid[sr][sc] == '1' or grid[tr][tc] == '1':
    print(-1)
    exit()

dist = [[-1]*M for _ in range(N)]
q = deque([(sr, sc)])
dist[sr][sc] = 0

while q:
    r, c = q.popleft()
    if (r, c) == (tr, tc):
        break
    for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
        nr, nc = r+dr, c+dc
        if 0 <= nr < N and 0 <= nc < M and grid[nr][nc] == '0' and dist[nr][nc] == -1:
            dist[nr][nc] = dist[r][c] + 1
            q.append((nr, nc))

print(dist[tr][tc])
