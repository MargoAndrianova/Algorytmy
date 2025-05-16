from collections import deque
from random import random, randint


def read_ints():
    return list(map(int, input().split()))

n, m = read_ints()
px, py = read_ints()
vx, vy = read_ints()

# Переведення до 0-індексації
px -= 1; py -= 1
vx -= 1; vy -= 1

maze = [read_ints() for _ in range(n)]

dirs = [(-1,0), (1,0), (0,-1), (0,1)]

def bfs(sx, sy):
    dist = [[-1]*m for _ in range(n)]
    q = deque([(sx, sy)])
    dist[sx][sy] = 0
    while q:
        x, y = q.popleft()
        for dx, dy in dirs:
            nx, ny = x+dx, y+dy
            if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] == 0 and dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx, ny))
    return dist

dist_p = bfs(px, py)
dist_v = bfs(vx, vy)

best_time = float('inf')
meet = (-1, -1)
another = []

for i in range(n):
    for j in range(m):
        dp = dist_p[i][j]
        dv = dist_v[i][j]
        # шукаємо точки, де обидва прибувають одночасно
        if dp != -1 and dv != -1:
            if max(dp,dv) < best_time:
                best_time = max(dp,dv)
                meet = (i, j)
            elif max(dp,dv) == best_time:
                another.append((i, j))
another.append(meet)
another.sort()
l = len(another) - 1

if meet == (-1, -1):
    print(-1)
else:
    meet_pl = another[randint(0, l)]
    print(meet_pl[0] + 1, meet_pl[1] + 1)
