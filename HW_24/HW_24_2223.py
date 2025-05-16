from collections import deque

def read():
    h, m, n = map(int, input().split())
    levels = []
    for lvl in range(h):
        level = []
        for _ in range(m):
            level.append(list(input().rstrip()))
        levels.append(level)
        if lvl != h - 1:
            input()
    return h, m, n, levels

h, m, n, lab = read()

start = None
end = None
for z in range(h):
    for x in range(m):
        for y in range(n):
            if lab[z][x][y] == '1':
                start = (z, x, y)
                lab[z][x][y] = '.'
            elif lab[z][x][y] == '2':
                end = (z, x, y)
                lab[z][x][y] = '.'

dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

visited = [[[False for _ in range(n)] for _ in range(m)] for _ in range(h)]
q = deque()
q.append((*start, 0))
visited[start[0]][start[1]][start[2]] = True

while q:
    z, x, y, time = q.popleft()

    if (z, x, y) == end:
        print(time)
        break

    for dx, dy in dirs:
        nx, ny = x + dx, y + dy
        if 0 <= nx < m and 0 <= ny < n:
            if lab[z][nx][ny] == '.' and not visited[z][nx][ny]:
                visited[z][nx][ny] = True
                q.append((z, nx, ny, time + 5))

    if z + 1 < h:
        if lab[z + 1][x][y] == '.' and not visited[z + 1][x][y]:
            visited[z + 1][x][y] = True
            q.append((z + 1, x, y, time + 5))