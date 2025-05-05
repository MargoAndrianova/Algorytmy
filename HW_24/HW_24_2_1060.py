from collections import deque

n = int(input())
grid = [list(input().rstrip()) for _ in range(n)]

start = end = None
for i in range(n):
    for j in range(n):
        if grid[i][j] == '@':
            start = (i, j)
        elif grid[i][j] == 'X':
            end = (i, j)

q = deque([start])
prev = [[None]*n for _ in range(n)]
visited = [[False]*n for _ in range(n)]
visited[start[0]][start[1]] = True

dirs = [(1,0),(-1,0),(0,1),(0,-1)]
found = False
while q:
    i, j = q.popleft()
    if (i, j) == end:
        found = True
        break
    for di, dj in dirs:
        ni, nj = i+di, j+dj
        if 0 <= ni < n and 0 <= nj < n and not visited[ni][nj]:
            if grid[ni][nj] in ('.', 'X'):
                visited[ni][nj] = True
                prev[ni][nj] = (i, j)
                q.append((ni, nj))

if not found:
    print("N")
else:
    i, j = end
    while (i, j) != start:
        grid[i][j] = '+'
        i, j = prev[i][j]
    print("Y")
    for row in grid:
        print(''.join(row))
