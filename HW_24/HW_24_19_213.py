from collections import deque

def read_input():
    H, W = map(int, input().split())
    grid = [list(input().rstrip()) for _ in range(H)]
    start1 = start2 = exit_pos = None
    for i in range(H):
        for j in range(W):
            c = grid[i][j]
            if c == '1':
                start1 = (i, j); grid[i][j] = '.'
            elif c == '2':
                start2 = (i, j); grid[i][j] = '.'
            elif c == '*':
                exit_pos = (i, j); grid[i][j] = '.'
    return H, W, grid, start1, start2, exit_pos

def bfs_escape(H, W, grid, s1, s2, exit_pos):
    dirs = [
        ('R', 0, 1),
        ('L', 0, -1),
        ('U', -1, 0),
        ('D',  1, 0)
    ]
    start = (s1[0], s1[1], s2[0], s2[1])
    goal  = (exit_pos[0], exit_pos[1], exit_pos[0], exit_pos[1])

    dq = deque([start])
    parent = {start: None}

    while dq:
        state = dq.popleft()
        if state == goal:
            return parent, True
        y1, x1, y2, x2 = state
        for cmd, dy, dx in dirs:
            ny1, nx1 = move_one(y1, x1, dy, dx, H, W, grid)
            ny2, nx2 = move_one(y2, x2, dy, dx, H, W, grid)
            new_state = (ny1, nx1, ny2, nx2)
            if new_state not in parent:
                parent[new_state] = (state, cmd)
                dq.append(new_state)

    return parent, False

def move_one(y, x, dy, dx, H, W, grid):
    ny, nx = y+dy, x+dx
    if 0 <= ny < H and 0 <= nx < W and grid[ny][nx] != '#':
        return ny, nx
    else:
        return y, x

def extract_path(parent, exit_pos):
    goal = (exit_pos[0], exit_pos[1], exit_pos[0], exit_pos[1])
    if goal not in parent:
        return None
    path = []
    cur = goal
    while parent[cur] is not None:
        prev_state, cmd = parent[cur]
        path.append(cmd)
        cur = prev_state
    path.reverse()
    return path

H, W, grid, s1, s2, exit_pos = read_input()
parent, ok = bfs_escape(H, W, grid, s1, s2, exit_pos)
if not ok:
    print(-1)
else:
    path = extract_path(parent, exit_pos)
    print(len(path))
    print(''.join(path))
